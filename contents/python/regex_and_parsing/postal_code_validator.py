"""
    Prompt: Check if postal codes are valid.
"""

import re

# P must be a number in the range from 100000 to 999999 inclusive.
regex_integer_in_range = r"^[1-9][0-9][0-9][0-9][0-9][0-9]$"

# P must not contain more than one alternating repetitive digit pair.
regex_alternating_repetitive_digit_pair = r"((\d)\d\2)|((\d)(\d)\4\5)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

print(re.findall(regex_alternating_repetitive_digit_pair, P))