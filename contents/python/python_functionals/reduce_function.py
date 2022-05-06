"""
    Prompt: Get the product of a list of fractions.
"""

import math
from fractions import Fraction
from functools import reduce

def product(fracs):
    # Do not use `.limit_denominator()` function for HackerRank problem set.
    t = math.prod(fracs)
    return t.numerator, t.denominator

if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)