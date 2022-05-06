"""
    Prompt: Print the start tag, its attributes, and the end tag for each element.
"""

import re
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for key, value in attrs:
            print("->", key, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for key, value in attrs:
            print("->", key, ">", value)

html = ""
for _ in range(int(input())):
    html += "\n" + input()

parser = MyHTMLParser()
matches = re.findall(r'(?<=(?:<!--\[if !IE 6\]><!-->))\s*.*?\s*(?=(?:<!--<!\[endif\]-->))', html)
if len(matches):
    for match in matches:
        parser.feed(match)
else:
    html = re.sub(r'(?<=(?:<!--\[if !IE 6\]><!-->))\s*.*?\s*(?=(?:<!--<!\[endif\]-->))', "", html)
    parser.feed(html)
parser.close()