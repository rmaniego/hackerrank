"""
    Prompt: Split a formatted decimal number.
"""
import re

regex_pattern = r"[\,\.]"
print("\n".join(re.split(regex_pattern, input())))