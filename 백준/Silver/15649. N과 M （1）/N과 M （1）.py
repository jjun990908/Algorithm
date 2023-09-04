N, M = map(int, input().split())
s = []


def dfs():
    if len(s) == M:
        print(*s)
        return
    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
