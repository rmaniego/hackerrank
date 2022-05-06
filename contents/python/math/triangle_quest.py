"""
    Prompt: Create triangle using 2 code lines and pure arithmetic.
"""
# Remove all comments and blank lines
# 11 is our important number
# We can get 11 through 1/3 (3.33~)
# Each step, we want 10**i
# Get the 1s by dividing with 3
# Print each (result * i) as integer
for i in range(1,int(input())):
    print(int(((1/3)*(10**i))//3*i))