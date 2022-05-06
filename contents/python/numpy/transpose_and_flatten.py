"""
    Prompt: Transpose and flatten array.
"""

import numpy as np

n, m = map(int, input().strip().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split(" "))))
arr = np.array(arr)

print(np.transpose(arr))
print(arr.flatten())