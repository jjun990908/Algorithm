import heapq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
items = []
for _ in range(N):
    a, b = map(int, input().split())
    items.append([a, b])
bags = [int(input()) for _ in range(K)]
items.sort()
bags.sort()
answer = 0
temp = []

for bag in bags:
    while items and items[0][0] <= bag:
        heapq.heappush(temp, -items[0][1])
        heapq.heappop(items)
    if temp:
        answer -= heapq.heappop(temp)
print(answer)
