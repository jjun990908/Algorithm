import sys

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [[0] * M for _ in range(N)]
answer = 0


def dfs(x, y, sum, depth):
    global answer
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    if depth == 4:
        answer = max(answer, sum)
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, sum + graph[nx][ny], depth + 1)
                visited[nx][ny] = 0


def check(x, y):
    global answer
    if x - 1 >= 0 and x + 1 < N and y + 1 < M:
        answer = max(
            answer, graph[x][y] + graph[x - 1][y] + graph[x + 1][y] + graph[x][y + 1]
        )
    if x - 1 >= 0 and x + 1 < N and y - 1 >= 0:
        answer = max(
            answer, graph[x][y] + graph[x - 1][y] + graph[x + 1][y] + graph[x][y - 1]
        )
    if x + 1 < N and y - 1 >= 0 and y + 1 < M:
        answer = max(
            answer, graph[x][y] + graph[x][y - 1] + graph[x][y + 1] + graph[x + 1][y]
        )
    if x - 1 >= 0 and y - 1 >= 0 and y + 1 < M:
        answer = max(
            answer, graph[x][y] + graph[x][y - 1] + graph[x][y + 1] + graph[x - 1][y]
        )


graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = 0
        check(i, j)
print(answer)
