N = int(input())
a = []
for _ in range(N):
    a.append(list(input().split()))
a.sort(key=lambda x: int(x[0]))
for i in a:
    print(i[0], i[1])