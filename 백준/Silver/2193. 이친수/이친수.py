import sys

input = sys.stdin.readline

N = int(input())
arr = [0, 1, 1]
for i in range(3, N + 1):
    arr.append(arr[i - 2] + arr[i - 1])
print(arr[N])
