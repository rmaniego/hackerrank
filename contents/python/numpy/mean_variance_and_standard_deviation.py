"""
    Prompt: Get the mean, variance, and standard deviation of axes 1, 0, and Non, respectively.
"""

import numpy as np

n, m = map(int, input().rstrip().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
arr = np.array(arr)

print(np.mean(arr, axis=1)) 
print(np.var(arr, axis=0)) 
print(round(np.std(arr), 11)) 