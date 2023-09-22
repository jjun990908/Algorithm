import sys

input = sys.stdin.readline

N = int(input())
tree = []

for _ in range(N):
    tree.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1):
        if i == 0:
            pass
        elif j == 0:
            tree[i][j] += tree[i - 1][j]
        elif j == i:
            tree[i][j] += tree[i - 1][j - 1]
        else:
            tree[i][j] += max(tree[i - 1][j], tree[i - 1][j - 1])

print(max(tree[N - 1]))
