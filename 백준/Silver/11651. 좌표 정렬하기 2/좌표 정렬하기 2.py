import sys

input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([y, x])

arr = sorted(arr)
for i, j in arr:
    print(j, i)
