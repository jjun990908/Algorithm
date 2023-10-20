from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = [0] * 101
height = 0
visited = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
highest = 0
for i in range(N):
    for j in range(N):
        highest = max(highest, board[i][j])


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        xx, yy = queue.pop()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and visited[nx][ny] == 0
                and board[nx][ny] > 0
            ):
                visited[nx][ny] = 1
                queue.append((nx, ny))


def heigthUP():
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                board[i][j] -= 1


for k in range(0, highest):
    height = k
    heigthUP()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and visited[i][j] == 0:
                answer[height] += 1
                bfs(i, j)
if max(answer) == 0:
    print("1")
else:
    print(max(answer))
