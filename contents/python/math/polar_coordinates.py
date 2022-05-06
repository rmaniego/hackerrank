"""
    Prompt: Print the polar coordinates of complex z.
"""

import cmath

num = complex(input())
r, phi = cmath.polar(num)

print(r)
print(phi)