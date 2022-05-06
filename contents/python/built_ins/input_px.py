"""
    Prompt: Check if P(x) is k.
    
    NOTE: For Python 2 only.
"""

import sys

if sys.version_info >= (3, 0):
    x, k = map(int, input().split(" "))
    formula = input().replace("x", str(x))
        
    print(eval(formula) == k)

else:
    lines = []
    for line in sys.stdin:
        lines.append(line)

    x, k = lines[0].split(" ")
    formula = lines[1].replace("x", x)

    print (eval(formula) == int(k))