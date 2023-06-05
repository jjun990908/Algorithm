import sys

input = sys.stdin.readline
N, M, B = map(int, input().split())
board = []
height = 0
answer = 999999999999
for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(257):
    use = 0
    dig = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] > i:
                dig += board[x][y] - i
            else:
                use += i - board[x][y]

    if use > dig + B:
        continue

    count = dig * 2 + use

    if count <= answer:
        answer = count
        height = i

print(answer, height)
