"""
    Prompt: Use divmod(a, b) and diplay q\nr\n(q, r)
"""
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    
    q, r = divmod(a, b)
    print(q, r, (q, r), sep="\n")