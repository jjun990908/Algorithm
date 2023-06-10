from sys import stdin


def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1

    else:
        return int(num)


n = int(stdin.readline())

if n == 0:
    print(0)
else:
    difficulties = []

    for _ in range(n):
        difficulties.append(int(stdin.readline()))

    difficulties.sort()

    cut = round(n * 0.15)

    if cut != 0:
        difficulties = difficulties[cut:-cut]

    answer = round(sum(difficulties) / (n - cut * 2))

    print(answer)
