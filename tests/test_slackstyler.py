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
        self._assert_converts_to('***bold+italic text***', '_*bold+italic text*_\n')

    def test_strike(self):
        self._assert_converts_to('~~strike text~~', '~strike text~\n')

    def test_unordered_list(self):
        self._assert_converts_to('* list item', '• list item\n')

    def test_ordered_list(self):
        self._assert_converts_to('1. list item', '1. list item\n')

    def test_link_with_title(self):
        self._assert_converts_to('[](http://atlassian.com "Atlassian")', '<http://atlassian.com|Atlassian>\n')

    def test_inline_code(self):
        self._assert_converts_to('hello `world`', 'hello `world`\n')

    def test_block_code(self):
        self._assert_converts_to('```\ncode block\n```', '```\ncode block\n```\n')

    def test_user_mention(self):
        self._assert_converts_to('<@UPXGB22A2>', '<@UPXGB22A2>\n')

    def test_escaped_text(self):
        self._assert_converts_to('*h&ello>world<', '*h&amp;ello&gt;world&lt;\n')

    def _assert_converts_to(self, text, expected):
        result = self.styler.convert(text)
        self.assertEqual(result, expected, 'Expected "{}" but got "{}"'.format(expected, result))


if __name__ == '__main__':
    unittest.main()
