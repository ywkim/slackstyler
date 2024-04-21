import unittest
from slackstyler import SlackStyler


class TestSlackStyler(unittest.TestCase):
    def setUp(self):
        self.styler = SlackStyler()

    def test_simple_text(self):
        self._assert_converts_to('hello world', 'hello world\n')

    def test_bold(self):
        self._assert_converts_to('**bold text**', '*bold text*\n')

    def test_italic(self):
        self._assert_converts_to('*italic text*', '_italic text_\n')

    def test_bold_italic(self):
        self._assert_converts_to('***bold+italic text***', '*_bold+italic text_*\n')

    def test_strike(self):
        self._assert_converts_to('~~strike text~~', '~strike text~\n')

    def test_unordered_list(self):
        self._assert_converts_to('* list item', '• list item\n')

    def test_ordered_list(self):
        self._assert_converts_to('1. list item\n2. list item', '1. list item\n2. list item\n')

    def test_link_with_title(self):
        self._assert_converts_to('[](http://atlassian.com "Atlassian")', '<http://atlassian.com|Atlassian>\n')

    def test_inline_code(self):
        self._assert_converts_to('hello `world`', 'hello `world`\n')

    def test_block_code(self):
        self._assert_converts_to('```\ncode block\n```', '```\ncode block\n```\n')

    def test_escaped_text(self):
        self._assert_converts_to('*h&ello>world<', '*h&amp;ello&gt;world&lt;\n')

    # New tests
    def test_header(self):
        self._assert_converts_to('## header', '*header*\n')

    def test_image_with_title(self):
        self._assert_converts_to('![](http://atlassian.com "Atlassian")', '<http://atlassian.com|Atlassian>\n')

    def test_autolink(self):
        self._assert_converts_to('<http://atlassian.com>', '<http://atlassian.com>\n')

    def _assert_converts_to(self, text, expected):
        result = self.styler.convert(text)
        self.assertEqual(result, expected, 'Expected "{}" but got "{}"'.format(expected, result))

    def test_links_with_content_text(self):
        self._assert_converts_to('[alt text](http://atlassian.com)', '<http://atlassian.com|alt text>\n')
    
    def test_links_with_content_and_title(self):
        self._assert_converts_to('[alt text](http://atlassian.com "Atlassian")',
                                 '<http://atlassian.com|alt text>\n')


if __name__ == '__main__':
    unittest.main()
