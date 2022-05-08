"""
    Day 5: Loops
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    for x in range(1, n+1):
        print(n, " x ", x, " = ", n*x, sep="")