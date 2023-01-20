N = int(input())
M = int(input())
computer = [[]for _ in range (0,N+1)]
virus = [0]*(N+1)
count = 0
for _ in range(M):
    a,b = map(int,input().split())
    computer[a] += [b]
    computer[b] += [a]

def dfs(n):
    virus[n] = 1
    for i in computer[n]:
        if(virus[i]==0):
            dfs(i)

dfs(1)
for i in virus:
    if(i == 1):
        count += 1
print(count-1)
