"""
    Day 6: Let's Review
"""

for _ in range(int(input())):
    S = input()
    even = "".join([S[i] for i in range(len(S)) if i%2==0])
    odd = "".join([S[i] for i in range(len(S)) if i%2!=0])
    
    print(even, odd)