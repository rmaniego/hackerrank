"""
    Prompt: Create a palindromic triangle using 2 code lines,
            with one for-loop and pure arithmetic only.
"""
# Remove all comments and blank lines
# The important number is 11/9
# Get palindromic length, ex. (1.22~)*100 = 122
# Remove the palindromic half, ex. 122//10 = 12
# Resize back to the palindromic length, ex. 12*10 = 120
# Sum the results with the (i-2, i-3,...,i-9)
# Not the best soltion, but is working with 1<=N<=9
# Remove all comments
for i in range(1, int(input())+1):
    print(int(((((a:=11/9)*(10**((i-1)*2)))//(c:=10**(i-1)))*c)+(((a*(10**((i-2)*2)))//(c:=10**(i-2)))*c)+(((a*(10**((i-3)*2)))//(c:=10**(i-3)))*c)+(((a*(10**((i-4)*2)))//(c:=10**(i-4)))*c)+(((a*(10**((i-5)*2)))//(c:=10**(i-5)))*c)+(((a*(10**((i-6)*2)))//(c:=10**(i-6)))*c)+(((a*(10**((i-7)*2)))//(c:=10**(i-7)))*c)+(((a*(10**((i-8)*2)))//(c:=10**(i-8)))*c))+(max(1*(i==9), 0)))