from collections import Counter

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    kind = []
    mul = 1
    for _ in range(N):
        arr.append(list(map(str, input().split())))
    for i, j in arr:
        kind.append(j)
    count = Counter(kind)
    for i in count:
        mul *= count[i] + 1
    print(mul - 1)
