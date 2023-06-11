import sys
from collections import Counter

input = sys.stdin.readline

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(input()))

print(round(sum(arr) / len(arr)))

arr.sort()

print(arr[len(arr) // 2])

count = Counter(arr).most_common(2)
if len(arr) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

print(max(arr) - min(arr))
