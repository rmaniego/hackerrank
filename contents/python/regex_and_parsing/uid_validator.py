"""
    Prompt: Check if UIDs are valid.
"""

import sys
import re

for _ in range(int(input())):
    number = input()
    # It should only contain alphanumeric characters.
    # There must be exactly 10 characters in a valid UID.
    if len(re.findall(r'^[a-zA-Z0-9]{10}$', number)):
        # No character should repeat. 
        if not len(re.findall(r'(?:([a-z])\w*\1)|(?:([A-Z])\w*\2)|(?:([0-9])\w*\3)', number)):
            # It must contain at least uppercase English alphabet characters.
            if len(re.findall(r'.*[A-Z].*[A-Z].*', number)):
                # It must contain at least uppercase English alphabet characters.
                if len(re.findall(r'.*[0-9].*[0-9].*[0-9].*', number)):
                    print("Valid")
                    continue
    print("Invalid")
sys.exit(0)