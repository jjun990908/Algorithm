import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    distance = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, [0, start])
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for line in graph[now]:
            temp = dist + line[1]
            if temp < distance[line[0]]:
                distance[line[0]] = temp
                heapq.heappush(queue, [temp, line[0]])
    return distance


answer = 0
for i in range(1, N + 1):
    a = dijkstra(i)
    b = dijkstra(X)
    answer = max(answer, a[X] + b[i])

print(answer)
