import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
answer = False
visited = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start, depth):
    global answer
    visited[start] = 1
    if depth == 5:
        answer = True
        return
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i, depth + 1)
    visited[start] = 0


for i in range(N):
    dfs(i, 1)
    if answer:
        break

if answer:
    print(1)
else:
    print(0)
