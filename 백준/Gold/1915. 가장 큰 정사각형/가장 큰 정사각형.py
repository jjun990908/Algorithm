from collections import deque
import heapq
import sys

# input = sys.stdin.readline
Y, X = map(int, input().split())
graph = []
for _ in range(Y):
    graph.append(list(map(int, list(input()))))
result = 0

for i in range(Y):
    for j in range(X):
        if i > 0 and j > 0 and graph[i][j] == 1:
            graph[i][j] += min(graph[i][j - 1], graph[i - 1][j], graph[i - 1][j - 1])
        result = max(result, graph[i][j])
print(result * result)
