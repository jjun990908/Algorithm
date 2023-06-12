import sys

input = sys.stdin.readline

N = int(input())
arr = [0, 1, 2]
for i in range(3, N + 1):
    arr.append((arr[i - 1] + arr[i - 2]) % 15746)
print(arr[N])
