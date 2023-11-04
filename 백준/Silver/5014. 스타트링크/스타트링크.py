from collections import deque
import sys

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)


def bfs():
    queue = deque()
    queue.append((S, 0))
    visited[S] = 1
    while queue:
        now, dist = queue.popleft()
        for dir in (U, -D):
            next = now + dir
            if 0 < next <= F and visited[next] == 0:
                visited[next] = dist + 1
                queue.append((next, dist + 1))
                # print(queue)
            # else:
            #     visited[next] = min(visited[next], dist + 1)


bfs()
if visited[G] == 0:
    print("use the stairs")
elif S == G:
    print(0)
else:
    print(visited[G])
