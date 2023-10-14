from collections import deque
import sys

MAX = int(1e9)
input = sys.stdin.readline

N = int(input())
boundary = list(map(int, input().split()))
grade = input()
record = []
for char in grade:
    if char == "B":
        record.append(0)
    elif char == "S":
        record.append(1)
    elif char == "G":
        record.append(2)
    elif char == "P":
        record.append(3)
    elif char == "D":
        record.append(4)

answer = 0
money = []
money = deque()
for i in record:
    if len(money) >= 2:
        money.popleft()
    if i != 4:
        temp = (boundary[i] - 1) - sum(money)
        answer += temp
        money.append(temp)
    elif i == 4:
        answer += boundary[3]
        money.append(boundary[3])
print(answer)
