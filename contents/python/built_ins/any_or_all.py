"""
    Check if the list contains all positive integers and if any is number is palindromic.
    Solve in 3 lines of code or less.
"""

s = int(input())
nums = input().rstrip().split(" ")
print(all([int(n)>0 for n in nums]) and any([n[:max(s//2,1)] == "".join(list(reversed(n[-(s//2):]))) for n in nums]))