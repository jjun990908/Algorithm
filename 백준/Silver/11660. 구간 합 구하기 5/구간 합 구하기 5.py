import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = []
sum = 0

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            board[i][j] += board[i][j - 1]
        elif j == 0:
            board[i][j] += board[i - 1][j]
        else:
            board[i][j] += board[i][j - 1] + board[i - 1][j] - board[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if x1 == 0 and y1 == 0:
        print(board[x2][y2])
    elif x1 == 0:
        print(board[x2][y2] - board[x2][y1 - 1])
    elif y1 == 0:
        print(board[x2][y2] - board[x1 - 1][y2])
    else:
        print(
            board[x2][y2]
            - board[x1 - 1][y2]
            - board[x2][y1 - 1]
            + board[x1 - 1][y1 - 1]
        )
