from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] = max(arr[i], arr[i - 1] + arr[i])
print(max(arr))
