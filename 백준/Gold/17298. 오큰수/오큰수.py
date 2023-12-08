from collections import deque
import heapq
import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
answer = [-1] * N
stack = deque()

for i in range(N):
    while stack and (stack[-1][0] < arr[i]):
        value, idx = stack.pop()
        answer[idx] = arr[i]
    stack.append([arr[i], i])

print(*answer)
