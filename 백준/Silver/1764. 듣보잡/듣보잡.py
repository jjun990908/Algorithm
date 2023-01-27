N, M = map(int, input().split())
a = set()
for _ in range(N):
    a.add(input())

b = set()
for _ in range(M):
    b.add(input())

answer = sorted(list(a&b))

print(len(answer))
for i in answer:
    print(i)