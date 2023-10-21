from collections import deque
import sys

input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    while queue:
        yy, xx = queue.popleft()
        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((ny, nx))
                count += 1
    return count


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1

answer = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] += 1
            answer.append(bfs(i, j))

print(len(answer))
print(*sorted(answer))
