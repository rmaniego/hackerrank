"""
    Prompt: Create a Rangoli pattern.
"""

def print_rangoli(size):
    m = ((size*2)-1)*2-1
    alpha = "abcdefghijklmnopqrstuvwxyz"[:size]
    for i in range(1, size+1):
        temp = "-".join(list("".join(reversed(alpha[size-i+1:])) + alpha[size-i:]))
        print(temp.center(m, "-"))
    for i in range(size-1, 0, -1):
        temp = "-".join(list("".join(reversed(alpha[size-i+1:])) + alpha[size-i:]))
        print(temp.center(m, "-"))

if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)