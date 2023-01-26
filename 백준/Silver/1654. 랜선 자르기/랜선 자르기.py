import sys
K, N = map(int, sys.stdin.readline().split())
a = []

for i in range(K):
    a.append(int(sys.stdin.readline()))

start = 1
end = max(a)

while (start <= end):
    mid = (start + end) // 2
    count = 0
    for i in range(K):
        count += a[i] // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)