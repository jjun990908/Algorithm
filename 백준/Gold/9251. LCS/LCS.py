import sys

input = sys.stdin.readline
line1 = input().rstrip()
line2 = input().rstrip()

N = len(line1)
N2 = len(line2)
log = [0] * N2

for i in range(N):
    temp = 0
    for j in range(N2):
        if temp < log[j]:
            temp = log[j]
        elif line1[i] == line2[j]:
            log[j] = temp + 1
print(max(log))
