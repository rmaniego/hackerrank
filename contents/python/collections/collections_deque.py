"""
    Prompt: Perform operations on a deque object.
"""

from collections import deque

n = int(input())

queue = deque()
for _ in range(n):
    cmd = input().rstrip()
    if "appendleft" in cmd:
        queue.appendleft(cmd.split(" ")[-1])
    elif "append" in cmd:
        queue.append(cmd.split(" ")[-1])
    elif cmd == "pop":
        queue.pop()
    elif cmd == "popleft":
        queue.popleft()
print(" ".join(queue))