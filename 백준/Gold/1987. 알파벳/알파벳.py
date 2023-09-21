R, C = map(int, input().split())
board = []
visited = [-1 for _ in range(26)]
for _ in range(R):
    board.append(list(input()))


def modify(text):
    return ord(text) - 65


answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and visited[modify(board[nx][ny])] == -1:
            visited[modify(board[nx][ny])] = 1
            dfs(nx, ny, count + 1)
            visited[modify(board[nx][ny])] = -1


visited[modify(board[0][0])] = 1
dfs(0, 0, 1)

print(answer)