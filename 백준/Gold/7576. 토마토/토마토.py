from collections import deque

M,N = map(int, input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
day = 0

queue = deque([])
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            queue.append([i,j])

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            next_x = dx[i]+x
            next_y = dy[i]+y
            if 0<= next_x < N and 0<=next_y<M and tomato[next_x][next_y]==0:
                queue.append([next_x,next_y])
                tomato[next_x][next_y] = tomato[x][y]+1

bfs()

for i in range(N):
    for j in range(M):
        if tomato[i][j]==0:
            print(-1)
            exit(0)
        else:
            day = max(day,tomato[i][j])


print(day-1)