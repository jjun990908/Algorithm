from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
answer = 1
board = []
visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    board.append(list(map(int, input().split())))

while 1:
    flag = 0
    for i in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                answer += 1
                r = nx
                c = ny
                flag = 1
                break
    if flag == 0:
        if board[r - dx[d]][c - dy[d]] == 1:
            print(answer)
            break
        else:
            r = r - dx[d]
            c = c - dy[d]
