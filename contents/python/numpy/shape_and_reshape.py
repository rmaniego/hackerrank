"""
    Prompt: Reshape 1D array into a 3x3 matrix.
"""

import numpy as np

arr = list(map(int, input().strip().split(" ")))
print(np.reshape(np.array(arr), (3, 3)))