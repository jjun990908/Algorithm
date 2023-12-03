from collections import deque
import heapq
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
S = list(map(int, input().split()))
S.sort()
distance = []
for i in range(1, N):
    distance.append(S[i] - S[i - 1])
distance.sort(reverse=True)

print(sum(distance[K - 1 :]))
