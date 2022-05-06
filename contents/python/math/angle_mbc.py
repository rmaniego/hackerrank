"""
    Prompt: Print the polar coordinates of complex z.
"""

import math

ab = int(input())
bc = int(input())
ac = math.sqrt(ab**2 + bc**2)

A = round(math.degrees(math.asin(ab/ac)))
print(f"{A}\u00B0")