"""
    Prompt: Find the Captain's Room.
"""
if __name__ == "__main__":    
    
    """
    _ = int(input())
    tourists = [x for x in input().split(" ")]
    half = len(tourists) // 2
    A = set(tourists[0:half])
    B = set(tourists[half:])
    captain = ((A - B) | (B - A))
    print(list(captain)[0])
    """

    rooms = {}
    K = int(input())
    for room in input().split(" "):
        rooms[room] = rooms.get(room, 0) + 1
    for room, count in rooms.items():
        if count != K:
            print(room)
            break  