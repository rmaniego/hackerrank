"""
    Prompt: Check if a/b will generate an excpetion.
"""

import re


for _ in range(int(input())):
    try:
        a, b = map(int, input().strip().split(" "))
        print(a//b)
    except Exception as e:
        print("Error Code:", e)