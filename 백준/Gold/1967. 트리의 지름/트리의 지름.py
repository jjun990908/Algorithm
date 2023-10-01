from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited = [-1] * (N + 1)
    visited[start] = 1
    result = [0, 0]
    while queue:
        node, cost = queue.popleft()
        for nextNode, nextCost in graph[node]:
            if visited[nextNode] == -1:
                sumCost = cost + nextCost
                queue.append((nextNode, sumCost))
                visited[nextNode] = 1
                if result[1] <= sumCost:
                    result[0] = nextNode
                    result[1] = sumCost
    return result


node, cost = bfs(1)
print(bfs(node)[1])
