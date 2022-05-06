"""
    Prompt: Count the total attributes of the root and nested tags.
"""

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)
    for el in node:
        score += get_attr_number(el)
    return score

# Do not use code below, for testing only.
if __name__ == "__main__":
    xml = ""
    for _ in range(int(input())):
        xml += "\n" + input()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))