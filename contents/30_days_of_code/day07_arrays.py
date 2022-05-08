"""
    Day 7: Arrays
"""

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    print(" ".join(list(map(str, reversed(arr)))))
