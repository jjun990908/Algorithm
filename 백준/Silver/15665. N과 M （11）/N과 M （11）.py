N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
temp = []


def dfs():
    if len(temp) == M:
        print(*temp)
        return
    for i in range(len(arr)):
        temp.append(arr[i])
        dfs()
        temp.pop()


dfs()
