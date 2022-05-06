"""
    Prompt: Check if A is a subset of B.
"""


for _ in range(int(input())):
    _ = input()
    a = set(map(int, input().split()))
    
    _ = input()
    b = set(map(int, input().split()))
    
    print(not(bool(a-b)))