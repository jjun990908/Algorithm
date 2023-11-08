from collections import deque
import sys

input = sys.stdin.readline


def union(x, y):
    xx = find(x)
    yy = find(y)
    if xx >= yy:
        parents[xx] = yy
    else:
        parents[yy] = xx


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


N = int(input())
M = int(input())

parents = [i for i in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            union(i, j)

parents = [-1] + parents
path = list(map(int, input().split()))
start = parents[path[0]]
for i in range(1, M):
    if parents[path[i]] != start:
        print("NO")
        break
else:
    print("YES")
