import re
import sys

lines = sys.stdin.read()

pattern = r'(?:\/\/[\s\S]*?(?=(?:[\r\n]|$)))|(?:\/\*[\s\S]*?\*\/)'
for match in re.findall(pattern, lines):
    comment = [x.strip() for x in match.split("\n")]
    print("\n".join(comment))