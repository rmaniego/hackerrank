"""
    Prompt: Perform N operations in set A.
"""
if __name__ == "__main__":    
    # A.update(B) or A |= B
    # A.intersection_update(B) or A &= B
    # A.difference_update(B) or A -= B
    # A.symmetric_difference_update(B) or A ^= B
    
    _ = int(input())
    A = set(map(int, set(input().split(" ")) - {"", " "}))
    for _ in range(int(input())):
        cmd = input().split(" ")
        B = set(map(int, set(input().split(" ")) - {"", " "}))
        if cmd[0] == "update":
            A |= B
        elif cmd[0] == "intersection_update":
            A &= B
        elif cmd[0] == "difference_update":
            A -= B
        elif cmd[0] == "symmetric_difference_update":
            A ^= B
    print(sum(A))