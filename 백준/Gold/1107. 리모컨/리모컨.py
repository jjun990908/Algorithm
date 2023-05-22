import sys

input = sys.stdin.readline

target = int(input())
count = int(input())
diff = abs(target - 100)
if count:
    broken = list(map(str, input().split()))
else:
    broken = []

for i in range(1000001):
    for num in str(i):
        if num in broken:
            break
    else:
        diff = min(diff, len(str(i)) + abs(target - i))
print(diff)
