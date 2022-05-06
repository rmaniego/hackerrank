"""
    Prompt: Print the (start, end) indices for each match in string.
    (c) https://stackoverflow.com/a/63571450/4943299
"""
import re

string = input()
pattern = re.compile(input())
match = pattern.search(string)
if not match:
    print((-1, -1))

while match:
    print((match.start(), match.end()-1))
    match = pattern.search(string, match.start()+1)