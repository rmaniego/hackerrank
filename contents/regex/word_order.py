import re

conversations ="""hackerrank  abc 123 
abc hackerrank 123
abc 123 hackerrank
hackerrank
hackerrank hackerrank
123"""

patterns = [r'^hackerrank', r'^hackerrank*?$', r'hackerrank$']

# for _ in range(int(input())):
for conversation in conversation.split("\n"):
    # number = input()
    found = [0, 0, 0]
    for i in range(3):
        for match in re.findall(patterns[i], conversation):
            found[i] = 1
    if found[1] or (found[0] and found[2]):
        print(0)
    elif found[0]:
        print(1)
    elif found[2]:
        print(2)
    else:
        print(-1)