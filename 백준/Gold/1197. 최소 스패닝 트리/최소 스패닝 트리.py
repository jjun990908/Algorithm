from collections import deque
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
parents = [i for i in range(V + 1)]
lines = []
answer = 0
for _ in range(E):
    a, b, c = map(int, input().split())
    lines.append((a, b, c))
    graph[a].append((b, c))
    graph[b].append((a, c))
lines = sorted(lines, key=lambda x: x[2])


def find(x):
    if parents[x] == x:
        return x
    else:
        return find(parents[x])


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


for line in lines:
    if find(line[0]) != find(line[1]):
        answer += line[2]
        union(line[0], line[1])

print(answer)
