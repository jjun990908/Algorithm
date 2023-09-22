import copy
import sys

input = sys.stdin.readline

N = int(input())
a, b, c = map(int, input().split())
maxTree = [a, b, c]
minTree = [a, b, c]

for _ in range(N - 1):
    x, y, z = map(int, input().split())
    max_0 = x + max(maxTree[0], maxTree[1])
    min_0 = x + min(minTree[0], minTree[1])
    max_1 = y + max(maxTree)
    min_1 = y + min(minTree)
    max_2 = z + max(maxTree[1], maxTree[2])
    min_2 = z + min(minTree[1], minTree[2])
    maxTree = [max_0, max_1, max_2]
    minTree = [min_0, min_1, min_2]


print(max(maxTree), min(minTree))
