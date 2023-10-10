import heapq
import sys

input = sys.stdin.readline

MAX = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
distance = [MAX] * (N + 1)
vias = [0] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def djikstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for line in graph[now]:
            if dist + line[1] < distance[line[0]]:
                distance[line[0]] = dist + line[1]
                vias[line[0]] = now
                heapq.heappush(queue, (dist + line[1], line[0]))


djikstra(start)
print(distance[end])
answer = [end]
temp = end
while 1:
    if temp == start:
        break
    answer.append(vias[temp])
    temp = vias[temp]
print(len(answer))
answer.reverse()
print(*answer)
