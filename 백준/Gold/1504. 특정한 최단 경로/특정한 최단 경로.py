import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

N, E = map(int, input().split())
costs = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
V1, V2 = map(int, input().split())


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


planA = 0
planB = 0
dijkstra(1)
planA += costs[V1]
planB += costs[V2]
costs = [INF] * (N + 1)
dijkstra(V1)
planA += costs[V2]
planB += costs[N]
costs = [INF] * (N + 1)
dijkstra(V2)
planA += costs[N]
planB += costs[V1]
if min(planA, planB) >= INF:
    print(-1)
else:
    print(min(planA, planB))
