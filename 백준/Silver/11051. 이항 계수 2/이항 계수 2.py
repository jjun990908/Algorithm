import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= N
    N -= 1

div = 1
for i in range(2, K+1):
    div *= i

print((result // div) % 10007)