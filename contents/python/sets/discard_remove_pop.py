"""
    Prompt: Perform discard, remove, and pop in a set.
"""


_ = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd == "pop":
        s.pop()
    elif "remove" in cmd:
        value = int(cmd.split(" ")[-1])
        s.remove(value)
    elif "discard" in cmd:
        value = int(cmd.split(" ")[-1])
        s.discard(value)

print(sum(s))