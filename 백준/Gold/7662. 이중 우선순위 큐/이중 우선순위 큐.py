import heapq
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    minheap = []
    maxheap = []
    check = [1] * k
    for i in range(k):
        command, num = sys.stdin.readline().split()
        num = int(num)
        if command == "I":
            heapq.heappush(minheap, (num, i))
            heapq.heappush(maxheap, (-num, i))
        else:
            if len(minheap) != 0 and len(maxheap) != 0:
                if num == 1:
                    check[heapq.heappop(maxheap)[1]] = 0
                elif num == -1:
                    check[heapq.heappop(minheap)[1]] = 0
        while minheap and check[minheap[0][1]] == 0:
            heapq.heappop(minheap)
        while maxheap and check[maxheap[0][1]] == 0:
            heapq.heappop(maxheap)

    if len(minheap) != 0 and len(maxheap) != 0:
        print(-maxheap[0][0], minheap[0][0])
    else:
        print("EMPTY")
