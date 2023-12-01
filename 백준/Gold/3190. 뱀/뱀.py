from collections import deque
import heapq
import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
graph = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
L = int(input())
turn = []
for _ in range(L):
    time, dir = map(str, input().split())
    turn.append((int(time), dir))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir, x, y = 0, 0, 0
time, i = 0, 0
queue = deque()
queue.append((x, y))
while 1:
    x = x + dx[dir]
    y = y + dy[dir]
    time += 1
    if x < 0 or x >= N or y < 0 or y >= N or (x, y) in queue:
        break
    queue.append((x, y))
    if graph[x][y] == 0:
        queue.popleft()
    else:
        graph[x][y] = 0
    if time == turn[i][0]:
        if turn[i][1] == "L":
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        if i + 1 < len(turn):
            i += 1

print(time)
