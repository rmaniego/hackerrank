"""
    Prompt: Check if each set is strict superset of A.
    
    Strict Superset: At least 1 item in A is not present in B.
"""

strict_superset = []
a = set(map(int, input().split()))
for _ in range(int(input())):
    b = set(map(int, input().split()))
    strict_superset.append(not bool((b-a)) and bool(a-b))

print(all(strict_superset))