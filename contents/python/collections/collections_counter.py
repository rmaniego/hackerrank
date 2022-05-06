"""
    Prompt: Sell available shoes and print the sales.
"""

from collections import Counter

X = int(input())

sizes = Counter(input().strip().split(" "))

N = int(input())

shoes = []
for _ in range(N):
    size, price = input().strip().split(" ")
    if sizes[size] > 0:
        shoes.append(int(price))
        sizes[size] -= 1

print(sum(shoes))