import sys

input = sys.stdin.readline
N = int(input())
answer = 0
board = [0] * N


def isOkay(x):
    for i in range(x):
        if board[i] == board[x] or abs(board[i] - board[x]) == abs(i - x):
            return False
    return True


def queen(x):
    global answer
    if x == N:
        answer += 1
        return
    else:
        for i in range(N):
            board[x] = i
            if isOkay(x):
                queen(x + 1)


queen(0)
print(answer)
