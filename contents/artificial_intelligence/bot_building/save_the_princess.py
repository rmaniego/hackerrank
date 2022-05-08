"""
    Princess Peach is trapped in one of the four corners of a square grid.
    You are in the center of the grid and can move one step at a time
    in any of the four directions. Can you rescue the princess? 
"""

def displayPathtoPrincess(n,grid):
    princess = {}
    for i in range(n):
        if "p" in grid[i]:
            princess["y"] = i
            princess["x"] = grid[i].index("p")
    
    middle = int(n//2)
    rescuer = {}
    rescuer["x"] = middle
    rescuer["y"] = middle
    while (rescuer["x"] != princess["x"]) and (rescuer["y"] != princess["y"]):
        if rescuer["x"] > princess["x"]:
            rescuer["x"] -= 1
            print("UP")
        elif rescuer["x"] < princess["x"]:
            rescuer["x"] += 1
            print("DOWN")
        if rescuer["y"] > princess["y"]:
            rescuer["y"] -= 1
            print("LEFT")
        elif rescuer["y"] < princess["y"]:
            rescuer["y"] += 1
            print("RIGHT")
        

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)