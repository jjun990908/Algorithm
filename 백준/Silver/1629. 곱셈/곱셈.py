A, B, C = list(map(int, input().split()))


def square(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (square(a, b // 2, c)) ** 2 % c
    else:
        return (square(a, b // 2, c)) ** 2 * a % c


print(square(A, B, C))
