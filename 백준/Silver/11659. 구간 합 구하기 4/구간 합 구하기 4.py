import sys

input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))

b = [0] * (N + 1)
for i in range(N):
    b[i + 1] = b[i] + a[i]
 
for _ in range(M):
    i, j = map(int, input().split())
    print(b[j] - b[i - 1])