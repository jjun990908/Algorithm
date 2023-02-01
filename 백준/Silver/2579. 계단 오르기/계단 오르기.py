import sys

N = int(sys.stdin.readline())
stair = []
dp = []

for _ in range(N):
    stair.append(int(sys.stdin.readline()))

if len(stair)<=2:
    print(sum(stair))
else:
    dp.append(stair[0])
    dp.append(stair[0]+stair[1])
    dp.append(max(stair[0]+stair[2], stair[1]+stair[2]))
    for i in range(3, N):
        dp.append(max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i]))
    print(dp.pop())
