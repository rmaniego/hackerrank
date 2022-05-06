"""
    Prompt: Get the determinant of A.
"""

import numpy as np

n = int(input())

a = []
for _ in range(n):
    a.append(list(map(float, input().rstrip().split())))
a = np.array(a)

print(round(np.linalg.det(a), 2))