# slackstyler

![Python version](https://img.shields.io/badge/python-3.7-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

`slackstyler` is a Python package that converts Markdown text into Slack message formatting. The motivation for creating this package is to allow Python developers to prepare and send richly-formatted messages to Slack in a way that's familiar and easy to use.

`slackstyler` was inspired by JavaScript's `slackify-markdown` library and also based on `mistune`, a markdown parser in pure Python.

## Features
- Converts Markdown text into Slack message formatting.
- Supports various Markdown syntaxes:
  - **Bold text**
  - *Italic text*
  - [Link](http://atlassian.com)
  - and more...

## Installation
Install `slackstyler` with pip:
```bash
pip install slackstyler
```

## Usage

Here is a quick example of how to use `slackstyler`:

```python
from slackstyler import SlackStyler

# Create a styler instance
styler = SlackStyler()

# Convert markdown text to slack message text
markdown_text = "Hello, **Slack**!"
slack_message = styler.convert(markdown_text)
print(slack_message)
```

When you run this code, you will see:
```
Hello, *Slack*!
```

## Acknowledgments
This project was inspired by [`slackify-markdown`](https://github.com/jsarafajr/slackify-markdown), a similar library written in JavaScript.

## License

`slackstyler` is provided under the [MIT License](https://opensource.org/licenses/MIT).
