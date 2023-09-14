L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())

if n in S:
    print(0)
else:
    min = 0
    max = 0
    for num in S:
        if num < n:
            min = num
        elif num > n and max == 0:
            max = num
    max -= 1
    min += 1
    print((n - min) * (max - n + 1) + (max - n))
