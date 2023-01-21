from collections import deque

M,N,H = map(int, input().split())
tomato = [[list(map(int,input().split()))for _ in range(N)]for _ in range(H)]

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
day = 0

queue = deque([])
for i in range(H):
    for j in range(N):
        for k in range (M):
            if tomato[i][j][k]==1:
                queue.append((i,j,k))

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = dx[i]+x
            ny = dy[i]+y
            nz = dz[i]+z
            if 0<= nx < N and 0<=ny<M and 0<=nz<H and tomato[nz][nx][ny]==0:
                queue.append([nz,nx,ny])
                tomato[nz][nx][ny] = tomato[z][x][y]+1

bfs()

for i in tomato:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))

print(day-1)