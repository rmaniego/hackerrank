"""
    Prompt: Capitalize each word.
"""
import math
import os
import random
import re
import sys

def solve(s):
    words = []
    for x in s.split(" "):
        if len(x):
            words.append(x[0].upper() + x[1:])
        else:
            words.append("")
    return " ".join(words)

if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    print(solve(s))
    