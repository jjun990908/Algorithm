import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        dp[i] = 1
    else:
        temp = 0
        for j in range(i):
            if arr[j] < arr[i]:
                temp = max(temp, dp[j])
        dp[i] = temp + 1
print(max(dp))
