"""
    Prompt: Print all sonsonant-wrapped vowels from a string using regex.
"""
import re

pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

string = input()
matches = re.findall(pattern, string)
if len(matches):
    for match in matches:
        print(match)
else:
    print(-1)