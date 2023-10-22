from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
visited = [0] * N
line = list(map(int, input().split()))
delNode = int(input())
answer = 0
for i in range(N):
    if line[i] == -1:
        continue
    tree[line[i]].append(i)


def bfs(a):
    queue = deque()
    queue.append(a)
    visited[a] = 1
    while queue:
        now = queue.popleft()
        for node in tree[now]:
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)


bfs(delNode)

for i in range(N):
    if delNode in tree[i]:
        tree[i].remove(delNode)
    if len(tree[i]) == 0 and visited[i] == 0:
        answer += 1

print(answer)
