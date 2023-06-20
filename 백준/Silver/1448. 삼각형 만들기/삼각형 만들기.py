import sys

input = sys.stdin.readline

N = int(input())
straw = sorted([int(input()) for _ in range(N)], reverse=True)
answer = -1

for i in range(N - 2):
    if straw[i] < straw[i + 1] + straw[i + 2]:
        answer = straw[i] + straw[i + 1] + straw[i + 2]
        break
print(answer)
