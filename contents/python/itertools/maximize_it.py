"""
    Prompt: Print the result of MaxSum(Xi**2)%M
"""

from itertools import chain, product

x, M = map(int, input().split(" "))

squares = []
for i in range(x):
    temp = list([[x**2] for x in list(map(int, input().split(" ")))[1:]])
    if i:
        squares = [list(chain.from_iterable(x)) for x in product(squares, temp)]
    else:
        squares = temp

mods = []
for s in squares:
    mods.append(sum(s)%M)
print(max(mods))