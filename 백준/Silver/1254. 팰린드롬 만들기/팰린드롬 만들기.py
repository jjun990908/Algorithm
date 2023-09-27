import sys

input = sys.stdin.readline
S = input().rstrip()
for i in range(len(S)):
    if S[i:] == S[i:][::-1]:
        print(len(S) + i)
        break
