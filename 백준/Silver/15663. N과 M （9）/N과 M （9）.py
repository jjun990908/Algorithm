n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []


def dfs():
    if len(temp) == m:
        print(*temp)
        return
    prev = 0
    for i in range(n):
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            temp.append(arr[i])
            prev = arr[i]
            dfs()
            visited[i] = False
            temp.pop()


dfs()
