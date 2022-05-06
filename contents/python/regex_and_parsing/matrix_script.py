"""
    Prompt: Decode NxM matrix by removing non-alphanumeric characters between alphanumeric words.
"""
import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string = [""] * (n*m)
for i in range(n):
    line = list(matrix[i])
    for j in range(m):
        string[i+(n*j)] = line[j]

print(re.sub(r'(?<=\w)\W+(?=\w)', " ", "".join(string)))