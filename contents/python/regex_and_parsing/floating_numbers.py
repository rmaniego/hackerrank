"""
    Prompt: Check if a numeric string is a valid floating number.
"""
import re

for _ in range(int(input())):
    string = input()
    if len(re.findall(r'^[\+\-]{0,1}\d*\.\d+$', string)):
        print("True")
    else:
        print("False")