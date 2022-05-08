"""
    Day 10: Binary Numbers
"""

if __name__ == "__main__":
    print(len(str(max(list(map(int, [x for x in str(bin(int(input().strip())))[2:].split("0") if x.strip()]))))))