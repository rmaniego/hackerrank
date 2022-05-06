"""
    Prompt: Print the occurence of each character.
"""

from itertools import groupby

print(" ".join([str((len(list(y)), int(x))) for x, y in groupby(list(input()))]))