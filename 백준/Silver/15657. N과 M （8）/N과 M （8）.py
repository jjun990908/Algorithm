N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []


def dfs(n):
    if len(s) == M:
        print(*s)
        return
    for i in range(n, N + 1):
        s.append(arr[i - 1])
        dfs(i)
        s.pop()


dfs(1)
