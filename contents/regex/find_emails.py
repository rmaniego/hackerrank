# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

lines = ""
for _ in range(int(input())):
    lines += " " + input()

pattern = r'[\w.\-+]+\@[a-z]+?\.[a-z]+(?:\.[a-z]*)*\b'
matches = re.findall(pattern, lines)
matches = [x for x in matches if x.strip() != ""]
print(";".join(sorted(set(matches))))