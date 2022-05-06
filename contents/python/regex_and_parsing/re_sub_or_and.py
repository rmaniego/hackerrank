"""
    Prompt: Replace `||` and `&&` with `or` and `and`, respectively.
"""
import re

for _ in range(int(input())):
    html = re.sub("(?<=\s)\|\|(?=\s)", "or", input())
    print(re.sub("(?<=\s)\&\&(?=\s)", "and", html))