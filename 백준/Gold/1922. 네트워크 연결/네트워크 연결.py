import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
lines = []
parents = [i for i in range(N + 1)]
answer = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    lines.append((a, b, c))
lines = sorted(lines, key=lambda x: x[2])


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    xx = find(x)
    yy = find(y)
    # if xx >= yy:
    #     parents[x] = yy
    # else:
    #     parents[y] = xx
    parents[xx] = yy


for line in lines:
    if find(line[0]) != find(line[1]):
        answer += line[2]
        # print(line)
        union(line[0], line[1])

print(answer)
