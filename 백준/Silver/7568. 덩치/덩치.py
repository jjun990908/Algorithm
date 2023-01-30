N = int(input())

data = []
for _ in range(N):
    a, b = map(int, input().split())
    data.append((a, b))
for i in range(N):
    count = 1
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    print(count, end=" ")
