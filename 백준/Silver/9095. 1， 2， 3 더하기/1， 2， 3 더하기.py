import sys

def dfs(num):
    if arr[num] != 0:
        return arr[num]
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        arr[num] = dfs(num-1) + dfs(num-2) + dfs(num-3)
        return arr[num]
     
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = [0] * (n+1)
    answer = dfs(n)
    print(answer)