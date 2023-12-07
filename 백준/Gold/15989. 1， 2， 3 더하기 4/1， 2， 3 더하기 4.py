from collections import deque
import heapq
import sys

input = sys.stdin.readline

T = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(T):
    n = int(input())
    print(dp[n])
