import sys

N = int(input())
a = (list(map(int,input().split())))

a.sort()
answer = 0
for i in range(0,N):
    answer += sum(a[0:i+1])
print(answer)