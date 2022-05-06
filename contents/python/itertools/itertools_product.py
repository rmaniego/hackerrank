"""
    Prompt: Print the cartesian product of two lists.
"""

from itertools import product

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

print(" ".join([str(x) for x in product(a, b)]))