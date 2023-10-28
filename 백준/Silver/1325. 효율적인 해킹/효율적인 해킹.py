from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
relationship = [[] for _ in range(N + 1)]
result = []
for _ in range(M):
    A, B = map(int, input().split())
    relationship[B].append(A)

for i in range(1, N + 1):
    queue = deque([i])
    count = 1

    visited = [False] * (N + 1)
    visited[i] = True

    while queue:
        now = queue.popleft()
        for next in relationship[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                count += 1
    result.append(count)

max_count = max(result)
for i in range(N):
    if result[i] == max_count:
        print(i + 1)
