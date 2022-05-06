"""
    Prompt: Minion Game!
"""

def minion_game(string):
    size = len(string)
    kevin = sum(
        size-i
        for i in range(size)
            if string[i] in "AEIOU")
    stuart = sum(
        size-i
        for i in range(size)
            if string[i] not in "AEIOU")

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == "__main__":
    s = input()
    minion_game(s)