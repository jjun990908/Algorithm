import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
answer = []

def cut(x, y, N) :
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :
        cut(x, y, N//2)
        cut(x, y+N//2, N//2)
        cut(x+N//2, y, N//2)
        cut(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    answer.append(0)
  else :
    answer.append(1)

cut(0,0,N)
print(answer.count(0))
print(answer.count(1))