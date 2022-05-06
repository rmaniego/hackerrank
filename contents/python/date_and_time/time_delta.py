"""
    Prompt: Print day of week from a string date.
"""

# import math
# import os
# import random
# import re
# import sys

from datetime import datetime
import time

def time_delta(t1, t2):
    # Sun 10 May 2015 13:54:36 -0700
    dt1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return str(abs(int((dt1 - dt2).total_seconds())))
    

if __name__ == "__main__":
    for _ in range(int(input())):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)

    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
    """