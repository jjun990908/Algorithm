import sys

input = sys.stdin.readline

A, B = map(int, input().split())
answer = 1
while B != A:
    answer += 1
    temp = B
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2

    if temp == B:
        print(-1)
        break
else:
    print(answer)
