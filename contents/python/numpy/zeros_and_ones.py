"""
    Prompt: Create a matrix of zeroes and ones.
"""

import numpy as np


shape = list(reversed(list(map(int, input().rstrip().split()))))

zeros = None
for x in shape[1:]:
    if zeros is None:
        zeros = np.zeros((x, shape[0]), dtype = np.int64).tolist()
    else:
        zeros = [zeros for _ in range(x)]
print(np.array(zeros))

ones = None
for x in shape[1:]:
    if ones is None:
        ones = np.ones((x, shape[0]), dtype = np.int64).tolist()
    else:
        ones = [ones for _ in range(x)]
print(np.array(ones))