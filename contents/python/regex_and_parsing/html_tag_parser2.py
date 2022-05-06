"""
    Prompt: Print the element and comment data.
"""

import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip() != "":
            print(data)

    def handle_data(self, data):
        if data.strip() != "":
            print(">>> Data")
            print(data)

html = ""
for _ in range(int(input())):
    html += "\n" + input()

parser = MyHTMLParser()
parser.feed(html)
parser.close()