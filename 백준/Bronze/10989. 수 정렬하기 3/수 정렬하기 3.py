import sys

N = int(input())
index = [0] * 10000

for _ in range(N):
    n = int(sys.stdin.readline())
    index[n-1] = index[n-1]+1

for i in range(10000):
    if index[i] !=0:
        for j in range(index[i]):
            print(i+1)