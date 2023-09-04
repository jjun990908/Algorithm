N, M = map(int, input().split())
s = []


def dfs(n):
    if len(s) == M:
        print(*s)
        return
    for i in range(n, N + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()


dfs(1)
