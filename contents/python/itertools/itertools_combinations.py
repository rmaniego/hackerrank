"""
    Prompt: Print the k combinations of a string.
"""

from itertools import combinations

S, k = input().split(" ")

for i in range(1, int(k)+1):
    print("\n".join(sorted(["".join(sorted(x)) for x in combinations(list(S), i)])))