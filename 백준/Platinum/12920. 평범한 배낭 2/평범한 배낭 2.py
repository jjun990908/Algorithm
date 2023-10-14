import sys

input = sys.stdin.readline

N, M = map(int, input().split())
items = []
for _ in range(N):
    a, b, c = map(int, input().split())
    index = 1
    while c > 0:
        temp = min(c, index)
        items.append((a * temp, b * temp))
        c -= index
        index = index * 2
itemCount = len(items)

dp = [[0] * (M + 1) for _ in range(itemCount + 1)]
for i in range(1, itemCount + 1):
    weight, value = items[i - 1]
    for j in range(1, M + 1):
        if weight <= j:
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[i][M])
