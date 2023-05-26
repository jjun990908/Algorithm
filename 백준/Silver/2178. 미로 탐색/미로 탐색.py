import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [[0] * M for _ in range(N)]
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return print(graph[N - 1][M - 1])


bfs(0, 0)
