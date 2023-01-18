n = int(input())
time = []

for i in range(n):
    a, b = map(int, input().split())
    time.append([a, b])

time.sort(key = lambda x: x[0])
time.sort(key = lambda x: x[1])
answer = 1
end = time[0][1]
for i in range(1, n):
    if time[i][0] >= end:
        answer += 1
        end = time[i][1]
print(answer)