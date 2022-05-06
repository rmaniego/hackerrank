"""
    Prompt: Get the maximum value of the minimum values along axis 1.
"""

import numpy as np

n, m = map(int, input().rstrip().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
arr = np.array(arr)

nums = np.min(arr, axis=1)
print(np.max(nums))