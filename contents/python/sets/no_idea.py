"""
    Prompt: Calculate your happiness based on the sets of numbers.
"""

n, m = map(int, input().rstrip().split(" "))

# Duplicates are counted, do not cast to a set.
arr = list(map(int, input().rstrip().split(" ")))
a = set(map(int, input().rstrip().split(" ")))
b = set(map(int, input().rstrip().split(" ")))

happiness = 0
for i in arr:
    happiness += int((i in a))
    happiness -= int((i in b))

print(happiness)