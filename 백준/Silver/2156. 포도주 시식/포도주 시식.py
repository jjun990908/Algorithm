import sys

input = sys.stdin.readline

N = int(input())
wine = [0] * (N + 1)
dp = [0] * (N + 2)
for i in range(N):
    wine[i] = int(input())

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
if N != 1:
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])
    for i in range(3, N):
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])
print(max(dp))
