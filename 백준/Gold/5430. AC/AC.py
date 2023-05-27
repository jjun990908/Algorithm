import sys
from collections import deque

T = int(input())
for _ in range(T):
    empty = False
    check = 0
    command = str(sys.stdin.readline().rstrip())
    length = int(input())
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    for i in command:
        if empty:
            continue
        if i == "R":
            check += 1
        elif i == "D":
            if length == 0:
                print("error")
                empty = True
                continue
            elif queue:
                if check % 2 == 0:
                    queue.popleft()
                    continue
                else:
                    queue.pop()
                    continue
            else:
                print("error")
                empty = True
                continue
    if not empty:
        if check % 2 != 0:
            queue.reverse()
        print("[" + ",".join(queue) + "]")
