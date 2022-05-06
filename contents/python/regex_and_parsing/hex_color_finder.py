"""
    Prompt: Print all valid CSS HEX colors.
"""
import re

for _ in range(int(input())):
    css = input()
    for match in re.findall(r'((?<=[\ \t:])\#(?:(?:[a-fA-F0-9]{6})|[a-fA-F0-9]{3})(?=[\,\;\)]))', css):
        print(match)