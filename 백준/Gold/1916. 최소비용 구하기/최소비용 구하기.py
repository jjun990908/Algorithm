from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
costs = [int(1e9)] * (N + 1)

buses = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    buses[a].append([b, c])

start, end = map(int, input().split())


def dijkstra(start):
    queue = deque()
    queue.append((0, start))
    costs[start] = 0
    while queue:
        cost, now = queue.pop()
        if costs[now] < cost:
            continue
        for bus in buses[now]:
            temp = cost + bus[1]
            if temp < costs[bus[0]]:
                costs[bus[0]] = temp
                queue.append((temp, bus[0]))


dijkstra(start)
print(costs[end])
