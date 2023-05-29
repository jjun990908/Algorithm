import sys
from collections import deque

sys.setrecursionlimit(10000)

input = sys.stdin.readline
N = int(input())
graph = []
answer = 0
answer2 = 0
now = ""
visited = [[0] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(str, input().strip())))


def dfs(x, y, color):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    if visited[x][y] == 0:
        visited[x][y] = 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if visited[nx][ny] == 0 and graph[nx][ny] == color:
                dfs(nx, ny, color)


def dfs_v2(x, y, color):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    if visited[x][y] == 0:
        visited[x][y] = 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if color == "B":
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    dfs_v2(nx, ny, color)
            else:
                if visited[nx][ny] == 0 and (
                    graph[nx][ny] == "R" or graph[nx][ny] == "G"
                ):
                    dfs_v2(nx, ny, color)


for i in range(N):
    for j in range(N):
        now = graph[i][j]
        if visited[i][j] == 0:
            answer += 1
        dfs(i, j, now)


visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        now = graph[i][j]
        if visited[i][j] == 0:
            answer2 += 1
        dfs_v2(i, j, now)

print(answer, answer2)
