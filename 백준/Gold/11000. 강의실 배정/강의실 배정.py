from collections import deque
import heapq
import sys

input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time = sorted(time)

room = []
heapq.heappush(room, time[0][1])
for i in range(1, N):
    if room[0] <= time[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, time[i][1])
print(len(room))
