"""
    Prompt: Check if RegEx is correct or not.
"""

import re

string = "test_string1234$$$$"
for _ in range(int(input())):
    try:
        re.findall(repr(input()), string)
        print("True")
    except:
        print("False")