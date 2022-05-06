"""
    Prompt: Print the k permutations of a string.
"""

from itertools import permutations

S, k = input().split(" ")

print(" \n".join(sorted(["".join(x) for x in permutations(list(S), int(k))])))