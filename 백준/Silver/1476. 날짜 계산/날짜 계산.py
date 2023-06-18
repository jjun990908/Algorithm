import sys

input = sys.stdin.readline

E, S, M = map(int, input().split())
answer = 1

while 1:
    if ((answer - E) % 15 == 0) and ((answer - S) % 28 == 0) and ((answer - M) % 19 == 0):
        break
    answer += 1

print(answer)
