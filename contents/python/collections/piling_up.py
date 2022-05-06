"""
    Prompt: Stack cubes.
"""

from collections import deque

T = int(input())

for _ in range(T):
    size = int(input())
    blocks = list(map(int, input().rstrip().split()))
    block = 2**31
    for _ in range(size):
        if (blocks[0] >= blocks[-1]) and (blocks[0] <= block):
            block = blocks[0]
            blocks.pop(0)
            continue
        if (blocks[-1] >= blocks[0]) and (blocks[-1] <= block):
            block = blocks[-1]
            blocks.pop(-1)
    if not len(blocks):
        print("Yes")
    else:
        print("No")