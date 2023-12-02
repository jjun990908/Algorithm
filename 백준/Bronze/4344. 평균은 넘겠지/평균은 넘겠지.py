from collections import deque
import heapq
import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    number = list(map(int, input().split()))
    avg = sum(number[1:]) / number[0]
    cnt = 0
    for score in number[1:]:
        if score > avg:
            cnt += 1
    answer = cnt / number[0] * 100
    print(f"{answer:.3f}%")
