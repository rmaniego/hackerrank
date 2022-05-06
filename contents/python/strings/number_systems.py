"""
    Prompt: Create a number system conversion table.
"""

def print_formatted(number):
    m = len(str(bin(number))[2:])
    for i in range(1, number+1):
        print(str(i).rjust(m), str(oct(i))[2:].rjust(m), str(hex(i))[2:].rjust(m).upper(), str(bin(i))[2:].rjust(m))

if __name__ == "__main__":
    n = int(input())
    print_formatted(n)