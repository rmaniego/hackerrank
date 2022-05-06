"""
    Prompt: Print the number with successive repetitions.
"""
import re

for _ in range(int(input())):
    html = input()
    matches = list(re.findall(r'([a-zA-Z0-9])\1', string))
    if matches:
        print(matches[0])
    else:
        print(-1)