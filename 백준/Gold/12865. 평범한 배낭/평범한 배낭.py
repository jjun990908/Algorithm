import sys

input = sys.stdin.readline
N, K = map(int, input().split())
items = []
for _ in range(N):
    items.append(list(map(int, input().split())))
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = items[i - 1]
        if w <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[i][K])
