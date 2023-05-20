import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-a, a))
