"""
    Sort string in this format: abcABC/Odd/Even/.
"""
import re

string = input()
odd = "".join(sorted(re.findall(r'[13579]', string)))
even = "".join(sorted(re.findall(r'[02468]', string)))
capital = "".join(sorted(re.findall(r'[A-Z]', string)))
lowercase = "".join(sorted(re.findall(r'[a-z]', string)))
print("".join([lowercase, capital, odd, even]))