import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= nx < Y) and (0 <= ny < X):
            if data[nx][ny] == 1:
                data[nx][ny] = 0
                dfs(nx, ny)


T = int(input())
for _ in range(T):
    X, Y, k = map(int, input().split())
    data = [[0]*X for _ in range(Y)]
    answer = 0
    for _ in range(k):
        a, b = map(int, input().split())
        data[b][a] = 1

    for i in range(Y):
        for j in range(X):
            if data[i][j] == 1:
                dfs(i, j)
                answer = answer + 1
    print(answer)
