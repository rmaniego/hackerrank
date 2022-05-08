"""
    Day 8: Dictionaries and Maps
"""

import sys

if __name__ == "__main__":
    n = int(input())
    
    phonebook = {}
    for _ in range(n):
        name, number = input().split()
        phonebook[name] = f"{name}={number}"

    for line in sys.stdin:
        print(phonebook.get(line.strip(), "Not found"))