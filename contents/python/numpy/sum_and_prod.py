"""
    Prompt: Get the product of the sum of axis.
"""

import numpy as np

n, m = map(int, input().rstrip().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
arr = np.array(arr)

sums = np.sum(arr, axis=0)
print(np.prod(sums))