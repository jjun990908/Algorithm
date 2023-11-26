from collections import deque
import sys

input = sys.stdin.readline


n, m, k = map(int, input().split())
trash = [[0] * (m + 1) for _ in range(n + 1)]
answer = 0
for _ in range(k):
    x, y = map(int, input().split())
    trash[x][y] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j):
    queue = deque([[i, j]])
    trash[i][j] = 2  # visited
    result = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 < nx <= n and 0 < ny <= m and trash[nx][ny] == 1:
                queue.append([nx, ny])
                trash[nx][ny] = 2
                result += 1
    return result


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if trash[i][j] == 1:
            ans = bfs(i, j)
            answer = max(ans, answer)

print(answer)
