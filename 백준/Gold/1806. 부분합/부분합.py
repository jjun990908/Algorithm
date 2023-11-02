import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
MAX = int(1e9)
answer = MAX
count = 0
sum = 0
end = 0

for start in range(N):
    while sum < M and end < N:
        sum += arr[end]
        end += 1
    if sum >= M:
        answer = min(answer, end - start)
    sum -= arr[start]

if answer == MAX:
    print(0)
else:
    print(answer)
