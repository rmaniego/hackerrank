"""
    In this version of "Bot saves princess",
    Princess Peach and bot's position are randomly set.
    Can you save the princess?
"""
        
def nextMove(n, r, c, grid):
    rescuer = {}
    rescuer["y"] = r
    rescuer["x"] = c
    princess = {}
    for i in range(n):
        if "p" in grid[i]:
            princess["y"] = i
            princess["x"] = grid[i].index("p")

    while True:
        if rescuer["x"] > princess["x"]:
            return "UP"
        if rescuer["x"] < princess["x"]:
            return "DOWN"
        if rescuer["y"] > princess["y"]:
            return "LEFT"
        if rescuer["y"] < princess["y"]:
            return "RIGHT"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))