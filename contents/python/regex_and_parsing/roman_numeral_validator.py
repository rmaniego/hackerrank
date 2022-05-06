"""
    Prompt: Check if a numeric string is a valid Roman numeral.
"""
import re

number = input()
pattern = r"^M{0,3}(?:CM){0,1}D{0,3}(?:CD){0,1}C{0,3}(?:XC){0,1}L{0,1}X{0,3}(?:XL){0,1}(?:IX){0,1}V{0,3}(?:IV){0,1}I{0,3}$"
print(bool(re.findall(pattern, number)))