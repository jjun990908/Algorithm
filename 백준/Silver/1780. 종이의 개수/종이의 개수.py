import sys

minus = 0
zero = 0
plus = 0


def dfs(x, y, N):
    global minus, zero, plus
    target = graph[x][y]
    for i in range(x, N + x):
        for j in range(y, N + y):
            if graph[i][j] != target:
                for k in range(3):
                    for l in range(3):
                        cut = N // 3
                        dfs(x + (cut * k), y + (cut * l), cut)
                return
    if target == 1:
        plus = plus + 1
    elif target == 0:
        zero = zero + 1
    else:
        minus = minus + 1


input = sys.stdin.readline
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
dfs(0, 0, N)
print(minus)
print(zero)
print(plus)
