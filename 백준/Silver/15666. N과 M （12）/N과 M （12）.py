N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
temp = []


def dfs(n):
    if len(temp) == M:
        print(*temp)
        return
    for i in range(n, len(arr)):
        temp.append(arr[i])
        dfs(i)
        temp.pop()


dfs(0)
