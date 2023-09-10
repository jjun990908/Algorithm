N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
temp = []


def dfs(n):
    if len(temp) == M:
        print(*temp)
        return
    prev = 0
    for i in range(n, N):
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            temp.append(arr[i])
            prev = arr[i]
            dfs(i + 1)
            visited[i] = False
            temp.pop()


dfs(0)
