"""
    Prompt: Check if credit card numbers are valid.
"""

import sys
import re

for _ in range(int(input())):
    number = input()
    # It must start with a 4, 5 or 6.
    # It must contain exactly 16 digits.
    # It must only consist of digits (0-9). 
    # It may have digits in groups of 4, separated by one hyphen "-".
    # It must NOT use any other separator like ' ' , '_', etc.
    if len(re.findall(r'^[456][0-9]{3}(\-?)[0-9]{4}(\-?)[0-9]{4}(\-?)[0-9]{4}$', number)):
        # It must NOT have or more consecutive repeated digits. 
        if not len(re.findall(r'([0-9])\-?\1\-?\1\-?\1', number)):
            print("Valid")
            continue
    print("Invalid")
sys.exit(0)