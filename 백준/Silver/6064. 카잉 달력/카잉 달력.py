import sys

input = sys.stdin.readline


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    now_x, now_y = 1, 1
    answer = 0
    flag = False
    gcd = GCD(M, N)
    for i in range(0, (N // gcd + 1)):
        answer = M * i + x
        if (answer - y) % N == 0:
            print(answer)
            flag = True
            break
    if flag == False:
        print(-1)
