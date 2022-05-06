"""
    Check the average score of the students from different subjects.
"""

n, x = map(int, input().strip().split(" "))

scores = []
for _ in range(x):
    scores.append(map(float, input().strip().split(" ")))


for grade in zip(*scores):
    print(round(sum(grade)/x, 2))