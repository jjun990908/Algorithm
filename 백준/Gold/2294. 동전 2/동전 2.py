from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [10001] * (K + 1)
dp[0] = 0

for c in coins:
    for i in range(c, K + 1):
        if dp[i] > 0:
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
