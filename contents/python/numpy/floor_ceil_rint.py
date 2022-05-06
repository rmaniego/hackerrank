"""
    Prompt: Round off vectors using floor, ceil, and rint.
"""

import numpy as np
np.set_printoptions(legacy='1.13')

arr = np.array(list(map(float, input().rstrip().split())))

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))