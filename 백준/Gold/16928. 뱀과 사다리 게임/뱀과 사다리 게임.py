import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
ladder = []
snake = []
visited = [0] * 1000
for i in range(N):
    ladder.append(list(map(int, input().split())))
for i in range(M):
    snake.append(list(map(int, input().split())))
for i, j in ladder:
    visited[i - 1] = j
for i, j in snake:
    visited[i - 1] = j

queue = deque()
queue.append((0, 0))
while queue:
    now, answer = queue.popleft()
    if visited[now] > 1:
        for i in range(1, 7):
            queue.append((visited[now] + i - 1, answer + 1))
    elif visited[now] == 0:
        visited[now] = 1
        for i in range(1, 7):
            queue.append((now + i, answer + 1))
    if now == 99:
        print(answer)
        break
