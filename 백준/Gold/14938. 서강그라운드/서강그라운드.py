import heapq
import sys

MAX = int(1e9)
input = sys.stdin.readline

N, M, R = map(int, input().split())
score = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

answer = 0

for i in range(1, N + 1):
    distance = [MAX] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, i))
    distance[i] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for line in graph[now]:
            temp = dist + line[1]
            if temp < distance[line[0]]:
                distance[line[0]] = temp
                heapq.heappush(queue, (temp, line[0]))
    temp = 0
    for index, dist in enumerate(distance):
        if dist <= M:
            temp += score[index - 1]
    answer = max(answer, temp)
print(answer)
