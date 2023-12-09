from collections import deque
import heapq
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort(reverse=True)


def dfs(start):
    stack = [start]
    visited = [-1] * (N + 1)
    answer = [0] * (N + 1)
    cnt = 1

    while stack:
        node = stack.pop()

        if visited[node] == 1:
            continue

        visited[node] = 1

        answer[node] = cnt
        cnt += 1

        for next in graph[node]:
            if visited[next] == -1:
                stack.append(next)

    return answer


answer = dfs(R)

print(*answer[1:])
