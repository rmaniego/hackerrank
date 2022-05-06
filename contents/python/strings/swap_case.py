"""
    Prompt: Swap cases os string s.
"""

def swap_case(s):
    swapped = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in s:
        if x in uppercase:
            swapped += x.lower()
        else:
            swapped += x.upper()
    return swapped

if __name__ == "__main__":    
    s = input()
    result = swap_case(s)
    print(result)