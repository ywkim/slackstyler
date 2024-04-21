import mistune
import re
import urllib.parse


class SlackStyler:
    def __init__(self, renderer=None):
        self.renderer = renderer if renderer else SlackRenderer()
        self.markdown = mistune.Markdown(renderer=self.renderer)

    def convert(self, text):
        return self.markdown(text)


class SlackRenderer(mistune.Renderer):
    SPECIALS = {'&': '&amp;', '<': '&lt;', '>': '&gt;'}

    def escape_special(self, text):
        escaped = text
        for special, replacement in self.SPECIALS.items():
            text = text.replace(special, replacement)
        return text

    def header(self, text, level, raw=None):
        return '*' + text + '*\n'

    def emphasis(self, text):
        return '_' + text + '_'

    def double_emphasis(self, text):
        return '*' + text + '*'

    def strikethrough(self, text):
        return '~' + text + '~'

    def list(self, body, ordered=True):
        lines = body.split('\n')
        count = 0
        for i, line in enumerate(lines):
            if line.startswith('li: '):
                count += 1
                if ordered:
                    prefix = '{}. '.format(count)
                else:
                    prefix = '• '
                lines[i] = prefix + line[4:]
        return '\n'.join(lines)

    def list_item(self, text):
        # always use the same prefix "li: "
        return 'li: ' + text + '\n'

    def link(self, link, title, content):
        escaped_link = self.escape_special(link)
        if content:
            return f'<{escaped_link}|{content}>'
        if title:
            return f'<{escaped_link}|{title}>'
        return f'<{escaped_link}>'

    def image(self, src, title, text):
        escaped_src = self.escape_special(src)
        if title or text:
            return f'<{escaped_src}|{title if title else text}>'
        return f'<{escaped_src}>'

    def codespan(self, text):
        return '`' + text + '`'

    def block_code(self, text, lang):
        return '```' + '\n' + text + '\n' + '```\n'

    def paragraph(self, text):
        return text + '\n'

    def autolink(self, link, is_email):
        if is_email:
            return link
        else:
            return self.link(link, None, None)
