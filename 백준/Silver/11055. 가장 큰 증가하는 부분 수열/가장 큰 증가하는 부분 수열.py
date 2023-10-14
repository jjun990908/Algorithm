from collections import deque
import sys

MAX = int(1e9)
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [[] * N for _ in range(N)]
answer = [0] * (N + 1)
dp[0].append(arr[0])
answer[0] = arr[0]
for i in range(N):
    if i == 0:
        continue
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j]:
            answer[i] = max(answer[i], answer[j])
    answer[i] += arr[i]

print(max(answer))
