from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
start, end = map(int, input().split())
M = int(input())
answer = -1

tree = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(node, depth):
    global answer
    depth += 1
    visited[node] = 1
    if node == end:
        answer = depth
    for i in tree[node]:
        if not visited[i]:
            dfs(i, depth)


dfs(start, 0)
if answer == -1:
    print(-1)
else:
    print(answer - 1)
