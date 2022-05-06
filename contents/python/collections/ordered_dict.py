"""
    Prompt: Update and display the ordered inventory.
"""

from collections import OrderedDict

n = int(input())

inventory = OrderedDict()
for _ in range(n):
    data = input().rstrip().split()
    item = " ".join(data[:-1])
    inventory[item] = inventory.get(item, 0) + int(data[-1])

for item, price in inventory.items():
    print(item, price)