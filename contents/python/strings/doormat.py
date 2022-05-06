"""
    Prompt: Create a NxM doormat.
"""

n, m = map(int, input().split(" "))

design = ".|."
for i in range(0, (n//2)):
    print((design*(i*2+1)).center(m, "-"))
print("WELCOME".center(m, "-"))
for i in range((n//2)-1, -1, -1):
    print((design*(i*2+1)).center(m, "-"))