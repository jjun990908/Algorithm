N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []


def dfs():
    if len(s) == M:
        print(*s)
        return
    for i in range(N):
        s.append(arr[i])
        dfs()
        s.pop()


dfs()
