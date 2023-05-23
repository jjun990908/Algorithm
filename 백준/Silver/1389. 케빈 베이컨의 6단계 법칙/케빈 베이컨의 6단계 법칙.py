import sys
from collections import deque

input = sys.stdin.readline


def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        target = queue.popleft()
        for i in person[target]:
            if visited[i] == 0:
                visited[i] = visited[target] + 1
                queue.append(i)


N, M = map(int, input().split())
person = [[] for _ in range(N + 1)]
answer = []
for _ in range(M):
    a, b = map(int, input().split())
    person[a].append(b)
    person[b].append(a)

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    bfs(i)
    answer.append(sum(visited))

print(answer.index(min(answer))+1)
