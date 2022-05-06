"""
    Prompt: Get the average marks of all students.
    There is no penalty for solutions that are correct but have more than 4 lines.
"""

from collections import namedtuple

n = int(input())

Grades = namedtuple("Grades", ",".join([x.strip() for x in input().strip().split(" ") if x != ""]))

total = 0
for _ in range(n):
    student = [x.strip() for x in input().strip().split(" ") if x != ""]
    total += float(Grades(*student).MARKS)

print(total/n)