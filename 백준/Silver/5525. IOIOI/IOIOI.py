import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
S = str(input())
length = 2 * N + 1
sentence = "I" + (("OI") * N)
answer = 0
for i in range(0, M - length + 1):
    if S[i : i + length] == sentence:
        answer += 1
print(answer)
