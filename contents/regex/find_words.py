# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

lines = ""
for _ in range(int(input())):
    lines += " " + input()
    
words = []
for _ in range(int(input())):
    words.append(input())

for word in words:
    matches = re.findall(fr"\b{word}\b", lines)
    count = len([x for x in matches if x.strip() != ""])
    print(count)
