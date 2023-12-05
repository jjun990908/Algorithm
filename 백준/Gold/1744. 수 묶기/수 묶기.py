from collections import deque
import heapq
import sys

input = sys.stdin.readline

N = int(input())
plus = []
minus = []
one = []
answer = 0
for _ in range(N):
    number = int(input())
    if number > 1:
        plus.append(number)
    elif number <= 0:
        minus.append(number)
    else:
        one.append(number)

plus.sort(reverse=True)
minus.sort()

length_plus = len(plus)
length_minus = len(minus)
if length_plus % 2 == 1:
    answer += plus[length_plus - 1]
    for i in range(0, length_plus - 1, 2):
        answer += plus[i] * plus[i + 1]
else:
    for i in range(0, length_plus, 2):
        answer += plus[i] * plus[i + 1]

if length_minus % 2 == 1:
    answer += minus[length_minus - 1]
    for i in range(0, length_minus - 1, 2):
        answer += minus[i] * minus[i + 1]
else:
    for i in range(0, length_minus, 2):
        answer += minus[i] * minus[i + 1]

for n in one:
    answer += n

print(answer)
