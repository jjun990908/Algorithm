from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
start = 0
end = N - 1
answerSum = abs(arr[start] + arr[end])
answer = [arr[start], arr[end]]

while start < end:
    left = arr[start]
    right = arr[end]
    sum = left + right
    if abs(sum) < answerSum:
        answerSum = abs(sum)
        answer = [left, right]
        if answerSum == 0:
            break
    if sum < 0:
        start += 1
    else:
        end -= 1
print(*answer)
