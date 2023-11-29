from collections import deque
import heapq
import sys

input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxVal = int(-1e9)
minVal = int(1e9)


def dfs(i, arr):
    global add, sub, mul, div, maxVal, minVal
    if i == N:
        maxVal = max(maxVal, arr)
        minVal = min(minVal, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, arr + number[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, arr - number[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, arr * number[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(arr / number[i]))
            div += 1


dfs(1, number[0])

print(maxVal)
print(minVal)
