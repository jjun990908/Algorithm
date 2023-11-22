from collections import deque
import sys
input = sys.stdin.readline

t = int(input())


def bfs() :
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    queue = deque()
    queue.append((startX, startY))
    while queue :
        x, y = queue.popleft()
        if x == endX and y == endY :
            return matrix[x][y] -1 
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and matrix[nx][ny] == 0 :
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx,ny))
                
            
        
for _ in range(t) :
    l = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    matrix = [[0]*l for _ in range(l)]
    matrix[startX][startY] = 1
    print(bfs())