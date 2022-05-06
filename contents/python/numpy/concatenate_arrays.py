"""
    Prompt: Concatenate NxP and MxP.
"""

import numpy as np

n, m, p = map(int, input().rstrip().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))
a = np.array(a)

b = []
for _ in range(m):
    b.append(list(map(int, input().rstrip().split())))
b = np.array(b)

print(np.concatenate([a, b]))