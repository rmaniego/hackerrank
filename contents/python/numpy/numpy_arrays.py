"""
    Prompt: Reverse and display array of floats.
"""

import numpy

def arrays(arr):
    return numpy.array(list(map(float, list(reversed(arr)))), dtype=float)

arr = input().strip().split(" ")
result = arrays(arr)
print(result)