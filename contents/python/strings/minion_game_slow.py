"""
    Prompt: Minion Game!
"""
import re

def minion_game(string):
    matches = set()
    stuart, kevin = 0, 0
    for char in set(string):
        for i in range(0, len(string)):
            pattern = fr"{char}"+r"[A-Z]{"+str(i)+r"}"
            matches |= set(re.findall(pattern, string))
    for match in matches:
        if match[0] in "AEIOU":
            kevin += string.count(match)
            continue
        stuart += string.count(match)

    if stuart > kevin:
        print("Stuart", stuart)
        return
    print("Kevin", kevin)

if __name__ == "__main__":
    s = input()
    minion_game(s)