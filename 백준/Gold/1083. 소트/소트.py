from collections import deque
import heapq
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

for i in range(N):
    large = max(arr[i : min(N, i + S + 1)])
    idx = arr.index(large)
    for j in range(idx, i, -1):
        temp = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = temp
    S -= idx - i
    if S <= 0:
        break
print(*arr)
