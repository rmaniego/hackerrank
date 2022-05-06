"""
    Prompt: Get the dot product of two NxN matrices.
"""

import numpy as np

n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int, input().rstrip().split(" "))))
a = np.array(a)

b = []
for _ in range(n):
    b.append(list(map(int, input().rstrip().split(" "))))
b = np.array(b)

print(np.dot(a, b))