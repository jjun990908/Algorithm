N = int(input())
arr = [0] * (N + 1)
arr[1] = 1
for i in range(2, N + 1):
    j = 1
    minAnswer = 4
    while (j * j) <= i:
        temp = arr[i - (j * j)]
        minAnswer = min(minAnswer, temp)
        j += 1
    arr[i] = minAnswer + 1
print(arr[N])
