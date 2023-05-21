import sys

input = sys.stdin.readline

N = int(input())
before = list(map(int, input().split()))
after = sorted(list(set(before)))

dic = {after[i]: i for i in range(len(after))}

for i in before:
    print(dic[i], end=" ")
