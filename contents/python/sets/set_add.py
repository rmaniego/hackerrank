"""
    Prompt: Add items to the set and print the total number of items.
"""

n = int(input())

countries = set()
for _ in range(n):
    countries.add(input())

print(len(countries))