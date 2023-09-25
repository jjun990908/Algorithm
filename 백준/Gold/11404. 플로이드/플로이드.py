import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

N = int(input())
M = int(input())
buses = [[] for _ in range(N + 1)]
costs = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    buses[a].append([b, c])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            costs[i][j] = 0
        elif buses[i]:
            for bus in buses[i]:
                if bus[0] == j:
                    costs[i][j] = min(costs[i][j], bus[1])

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])


for i in range(1, N + 1):
    for j in range(1, N + 1):
        if costs[i][j] >= INF:
            costs[i][j] = 0
for answer in costs[1:]:
    print(*answer[1:])
