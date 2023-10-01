from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

x, y, sharkSize, answer, count = 0, 0, 2, 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            x = i
            y = j
            break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b, sharkSize):
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1
    food = []
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and visited[nx][ny] == 0
                and board[nx][ny] <= sharkSize
            ):
                visited[nx][ny] = 1
                distance[nx][ny] = distance[xx][yy] + 1
                queue.append((nx, ny))
                if board[nx][ny] < sharkSize and board[nx][ny] != 0:
                    food.append((nx, ny, distance[nx][ny]))
    return sorted(food, key=lambda x: (-x[2], -x[0], -x[1]))


while 1:
    shark = bfs(x, y, sharkSize)
    if len(shark) == 0:
        break
    a, b, distance = shark.pop()
    board[x][y] = 0
    board[a][b] = 0
    count += 1
    answer += distance
    x = a
    y = b
    if count == sharkSize:
        sharkSize += 1
        count = 0

print(answer)
