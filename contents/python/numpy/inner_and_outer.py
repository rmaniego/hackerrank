"""
    Prompt: Get the inner and outer product of two 1xN matrices.
"""

import numpy as np

a = np.array(list(map(int, input().rstrip().split())))
b = np.array(list(map(int, input().rstrip().split())))

print(np.inner(a, b))
print(np.outer(a, b))