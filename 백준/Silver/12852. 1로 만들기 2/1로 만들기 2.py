from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
queue = deque()
queue.append([N])
answer = []

while queue:
    a = queue.popleft()
    x = a[0]
    if x == 1:
        answer = a
        break
    if x % 3 == 0:
        queue.append([x // 3] + a)
    if x % 2 == 0:
        queue.append([x // 2] + a)
    queue.append([x - 1] + a)

print(len(answer) - 1)
print(*answer[::-1])
