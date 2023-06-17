import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i][j] += arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1]

for _ in range(int(input())):
    i, j, k, l = map(int, input().split())
    print(arr[k][l] - arr[i - 1][l] - arr[k][j - 1] + arr[i - 1][j - 1])
