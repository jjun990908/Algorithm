from collections import deque
import sys

input = sys.stdin.readline


def bfs(start, group):
    queue = deque([start])
    visited[start] = group
    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if not visited[node]:
                queue.append(node)
                visited[node] = -1 * visited[x]
            elif visited[node] == visited[x]:
                return False
    return True


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:
            answer = bfs(i, 1)
            if not answer:
                break
    if answer:
        print("YES")
    else:
        print("NO")
