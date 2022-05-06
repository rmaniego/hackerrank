"""
    Prompt: Get the polynomial coefficient at point x.
"""

import numpy as np

a = np.array(list(map(float, input().rstrip().split())))
b = int(input())

print(np.polyval(a, b))