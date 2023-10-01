from collections import deque
import copy
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = []
answer = 0
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    queue = deque()
    temp = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                queue.append((i, j))
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))
    global answer
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1
    answer = max(answer, count)


def wall(count):
    if count == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    wall(count + 1)
                    board[i][j] = 0


wall(0)
print(answer)
