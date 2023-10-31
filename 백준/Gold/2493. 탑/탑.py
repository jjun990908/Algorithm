from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
answer = []
for index, value in enumerate(arr):
    if index == 0:
        stack.append((index, value))
        answer.append(0)
        continue
    while stack and stack[-1][1] < value:
        if len(stack) == 0:
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][0] + 1)
    stack.append((index, value))

print(*answer)
