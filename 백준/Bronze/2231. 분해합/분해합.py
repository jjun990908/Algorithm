N = int(input())
for i in range(1, N + 1):
    answer = i + sum((map(int, str(i))))
    if answer == N:
        print(i)
        break
    if i == N:
        print(0)
