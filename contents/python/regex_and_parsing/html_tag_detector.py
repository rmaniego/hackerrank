"""
    Prompt: Print all tag names and its attributes.
"""

import re
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for key, value in attrs:
            print("->", key, ">", value)

html = ""
for _ in range(int(input())):
    html += "\n" + input()

html = re.sub(r'[\ \t]*<!--.*-->[\r\n]*', "", html)
parser = MyHTMLParser()
parser.feed(html)
