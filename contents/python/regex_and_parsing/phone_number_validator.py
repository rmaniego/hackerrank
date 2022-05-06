"""
    Prompt: Check if a numeric string is a valid phone number.
"""
import re

for _ in range(int(input())):
    number = input()
    if len(re.findall(r'^[789]\d{9}$', number)):
        print("YES")
    else:
        print("NO")