"""
    Prompt: Display the indices of the values of B in A.
"""

from collections import defaultdict

n, m = map(int, input().strip().split(" "))

words = defaultdict(list)
# words["A"] = []
for _ in range(n):
    words["A"].append(input())


for _ in range(m):
    b = input().strip()
    indices = [str(i+1) for i in range(n) if words["A"][i] == b]
    if len(indices):
        print(" ".join(indices))
        continue
    print(-1)