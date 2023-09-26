import sys

input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))
target = int(input())
answer = 0
left = 0
right = N - 1

while left < right:
    if arr[left] + arr[right] == target:
        answer += 1
        left += 1
        right -= 1
    elif arr[left] + arr[right] > target:
        right -= 1
    elif arr[left] + arr[right] < target:
        left += 1

print(answer)
