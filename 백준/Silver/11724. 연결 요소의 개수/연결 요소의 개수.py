import sys

sys.setrecursionlimit(10000)


def dfs(start):
    result[start] = 1
    for i in data[start]:
        if result[i] == 0:
            dfs(i)


input = sys.stdin.readline
N, M = map(int, input().split())
data = [[] for _ in range(N + 1)]
result = [0] * (N + 1)
answer = 0
for _ in range(M):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)

for i in range(1, N + 1):
    if result[i] == 0:
        answer = answer + 1
        if data[i] == []:
            result[i] = 1
        else:
            dfs(i)

print(answer)