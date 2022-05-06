"""
    Prompt: Generate all [[i, j, k]] permutations where SUM(i, j, k) != n;
"""
if __name__ == "__main__":
    x = int(input()) + 1 # 0 <= i <= x
    y = int(input()) + 1 # 0 <= j <= y
    z = int(input()) + 1 # 0 <= k <= z
    n = int(input())
    
    # list comprehensions follows native list nested loops
    triplets = [[i, j, k]
    for i in range(x)
        for j in range(y)
            for k in range(z)
                if (i+j+k) != n]

    # equivalent to this one
    # triplets = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if (i+j+k) != n]
    print(triplets)