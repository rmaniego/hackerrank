import re

pans ="""ABCDS1234Y
ABAB12345Y
avCDS1234Y"""

pattern = r'^[A-Z]{5}\d{4}[A-Z]$'

# for _ in range(int(input())):
for number in pans.split("\n"):
    # number = input()
    if len(re.findall(pattern, number)):
        print("YES")
    else:
        print("NO")