N = int(input())
num = list(map(int, input().split()))
M = max(num)

for i in range(N):
    num[i] = num[i] / M * 100

print(sum(num) / N)
