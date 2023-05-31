import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
S = str(input())
answer = 0
i = 0
count = 0
while 1:
    if S[i : i + 3] == "IOI":
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0
    if (i + 3) >= M:
        break
print(answer)
