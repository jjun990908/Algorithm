import sys

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
selected = []


def dfs(start):
    global answer
    if sum(selected) == S and len(selected) > 0:
        answer += 1
    for i in range(start, N):
        selected.append(arr[i])
        dfs(i + 1)
        selected.pop()


dfs(0)
print(answer)
