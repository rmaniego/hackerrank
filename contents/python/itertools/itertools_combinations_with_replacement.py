"""
    Prompt: Print the k combinations with replacement of a string.
"""

from itertools import combinations_with_replacement

S, k = input().split(" ")

print("\n".join(sorted(["".join(sorted(x)) for x in combinations_with_replacement(list(S), int(k))])))