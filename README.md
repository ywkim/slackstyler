# slackstyler

## Description

`slackstyler` is a Python package that converts strings written in Markdown into Slack message formatting. It provides a simple and convenient conversion of Markdown styles into Slack styles, making it an effective tool when creating or integrating with Slack bots.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install slackstyler.

```bash
pip install slackstyler
```

## Usage

To use `slackstyler`, you only need to input the string that you want to convert from Markdown to Slack formatting.

Here's a basic example:

```python
from slackstyler import SlackStyler

styler = SlackStyler()

markdown_string = "**Hello!** This is a `test` message from _markdown_."

slack_style_string = styler.convert(markdown_string)

print(slack_style_string)
```

This will return the following result:

```bash
*Hello!* This is a `test` message from _markdown_.
```

## Features

`slackstyler` handles converting multiple aspects of Markdown into Slack message formatting, including but not limited to:

- Bold text: `**bold**` in Markdown becomes `*bold*` in Slack.
- Italics: `_italics_` in Markdown becomes `_italics_` in Slack.
- Code blocks: `` `code` `` in Markdown becomes `` `code` `` in Slack.

## Contributing

We welcome contributions to `slackstyler`. If there are new features that you would like to add, or bugs that you have found, please open a new issue or submit a pull request.

## License

`slackstyler` is licensed under the MIT license.

Thank you for choosing and using `slackstyler`. We hope this package makes your work with Slack and Markdown more efficient and enjoyable.
