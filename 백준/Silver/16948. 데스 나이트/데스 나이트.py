from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[0] * n for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                if nx == r2 and ny == c2:
                    return graph[nx][ny]
                queue.append((nx, ny))
    return -1


print(bfs(r1, c1))
