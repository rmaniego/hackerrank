"""
    Prompt: Perform arithetic on vectors.
"""

import numpy as np

n, m = map(int, input().rstrip().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))
a = np.array(a)

b = []
for _ in range(n):
    b.append(list(map(int, input().rstrip().split())))
b = np.array(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)