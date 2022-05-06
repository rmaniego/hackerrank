"""
    Prompt: Print the symmetric difference in ascending order.
"""

_ = int(input())
a = set(map(int, input().rstrip().split(" ")))

_ = int(input())
b = set(map(int, input().rstrip().split(" ")))

c = a ^ b

print("\n".join(map(str, sorted(c))))