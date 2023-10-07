from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())


def count(N, num):
    if N < num:
        return 0
    count = 0
    while N >= num:
        count += N // num
        N = N // num
    return count


two = count(N, 2) - count(N - M, 2) - count(M, 2)
five = count(N, 5) - count(N - M, 5) - count(M, 5)
print(min(two, five))
