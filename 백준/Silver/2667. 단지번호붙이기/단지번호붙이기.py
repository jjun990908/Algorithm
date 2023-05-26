import sys
import heapq

input = sys.stdin.readline
N = int(input())
graph = []
answer = 0
for i in range(N):
    graph.append(list(map(int, input().strip())))


def dfs(x, y, answer):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph[x][y] = -answer
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >= 0 and nx < N and ny >= 0 and ny < N and graph[nx][ny] == 1:
            dfs(nx, ny, answer)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer = answer + 1
            dfs(i, j, answer)
count = [0] * (answer)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            continue
        count[-graph[i][j] - 1] = count[-graph[i][j] - 1] + 1
print(answer)
count = sorted(count)
for i in range(answer):
    print(count[i])
