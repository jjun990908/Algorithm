N = int(input())
A = list(map(int, input().split()))
arr = sorted(A)
answer = []
for i in range(N):
    idx = arr.index(A[i])
    answer.append(idx)
    arr[idx] = -1
print(*answer)
