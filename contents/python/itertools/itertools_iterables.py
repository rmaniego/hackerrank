"""
    Prompt: Print the k-th char occurences in k combinations of a string.
"""

from itertools import combinations

size = int(input())
chars = input().split(" ")
K = int(input()) - 1

indices = [i
            for i in range(size)
                if chars[i] =='a']

c = list(combinations(list(range(size)), K+1))
rate = len(set([
        x
        for x in c
            for i in indices
                if i in x])) / len(c)

print(f"{rate:.12f}")