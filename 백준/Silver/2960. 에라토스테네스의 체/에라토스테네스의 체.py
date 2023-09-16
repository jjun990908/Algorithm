N, K = map(int, input().split())
arr = []
answer = []
for i in range(N + 1):
    arr.append(i)
arr[1] = 0


def add(n):
    answer.append(arr[n])
    arr[n] = 0


# while 1:
for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(1, N // i + 1):
            if arr[i * j] != 0:
                add(i * j)
        # if len(answer) == K:
        #     break


print(answer[K - 1])
