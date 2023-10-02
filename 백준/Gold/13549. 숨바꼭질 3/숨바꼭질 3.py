from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 100001
distance = [-1] * MAX


def bfs(start):
    queue = deque()
    queue.append(start)
    distance[start] = 0
    while queue:
        now = queue.popleft()
        if now == K:
            return distance[now]
        for next in (now * 2, now - 1, now + 1):
            if 0 <= next < MAX and distance[next] == -1:
                if next == now * 2:
                    distance[next] = distance[now]
                    queue.appendleft(next)
                else:
                    distance[next] = distance[now] + 1
                    queue.append(next)


print(bfs(N))
