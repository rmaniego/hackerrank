"""
    Prompt: Check if a string contains a valid email address.
"""
import re
import email.utils

for _ in range(int(input())):
    string = input()
    matches = re.findall(r'(?<=<)[a-zA-Z](?:[\w\.\-]+)@[a-zA-Z]*\.[a-zA-Z]{1,3}(?=>)', string)
    if matches:
        name = list(re.findall(r'\w*(?=\s<)', string))[0]
        print(email.utils.formataddr((name, list(matches)[0])))