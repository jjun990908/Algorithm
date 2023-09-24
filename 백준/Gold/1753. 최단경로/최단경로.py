import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
costs = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    costs[start] = 0
    while queue:
        cost, now = heapq.heappop(queue)
        if costs[now] < cost:
            continue
        for line in graph[now]:
            temp = cost + line[1]
            if temp < costs[line[0]]:
                costs[line[0]] = temp
                heapq.heappush(queue, (temp, line[0]))


dijkstra(start)
for cost in costs[1:]:
    if cost == INF:
        print("INF")
    else:
        print(cost)
