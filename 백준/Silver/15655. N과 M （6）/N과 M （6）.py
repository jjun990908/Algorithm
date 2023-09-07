N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []


def dfs(n):
    if len(s) == M:
        print(*s)
        return
    for i in range(n, N):
        if arr[i] in s:
            continue
        s.append(arr[i])
        dfs(i + 1)
        s.pop()


dfs(0)
