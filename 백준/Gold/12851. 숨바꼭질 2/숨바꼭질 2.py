from collections import deque
import sys

MAX = int(1e9)
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100002
distance = [-1] * 100002

queue = deque()
queue.append(N)
visited[N] = 1
distance[N] = 0

while queue:
    now = queue.popleft()
    if now == K:
        break
    for next in (now * 2, now + 1, now - 1):
        if 0 <= next <= 100000:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                visited[next] = visited[now]
                queue.append(next)
            elif distance[next] == distance[now] + 1:
                visited[next] += visited[now]
print(distance[K])
print(visited[K])
