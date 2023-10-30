from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr2 = arr[::-1]
dp = [1] * N
dp2 = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        if arr2[i] > arr2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

answer = [0 for _ in range(N)]
for i in range(N):
    answer[i] = dp[i] + dp2[N - i - 1] - 1
print(max(answer))
