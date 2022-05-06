# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'\([+-]?(?:(?:(?:[1-8][0-9]|[0-9])(?:\.(?:\d+))?)|90(?:\.0+)?)\, [+-]?(?:(?:(?:1[0-7][0-9]|[1-9][0-9]|[0-9])(?:\.(?:\d+))?)|180(?:\.0+)?)\)'
for _ in range(int(input())):
    if len(re.findall(pattern, input())):
        print("Valid")
    else:
        print("Invalid")