from collections import deque
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N + 1)]
answer = [-1] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(start, visited):
    for line in tree[start]:
        if visited[line] == -1:
            visited[line] = start
            dfs(line, visited)


dfs(1, answer)

print(*answer[2:])
