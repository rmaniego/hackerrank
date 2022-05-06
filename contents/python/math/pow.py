"""
    Prompt: Use pow(a, b, m) and math.pow(a, b), then diplay results in two lines.
"""
import math

a = int(input()) # 1 <= a <= 10
b = int(input()) # 1 <= b <= 10
m = int(input()) # 2 <= m <= 1000

print(int(math.pow(a, b)))
print(pow(a, b, m))