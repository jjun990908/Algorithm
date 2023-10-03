from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
distance = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs(a, b):
    queue = deque()
    queue.append([a, b, 0])
    distance[a][b][0] = 1

    while queue:
        x, y, wall = queue.popleft()
        if x == N - 1 and y == M - 1:
            return distance[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and distance[nx][ny][wall] == 0:
                    distance[nx][ny][wall] = distance[x][y][wall] + 1
                    queue.append([nx, ny, wall])
                elif graph[nx][ny] == 1 and wall == 0:
                    distance[nx][ny][wall + 1] = distance[x][y][wall] + 1
                    queue.append([nx, ny, wall + 1])
    return -1


print(bfs(0, 0))
