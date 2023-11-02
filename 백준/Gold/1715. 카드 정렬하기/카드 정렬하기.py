from queue import PriorityQueue
import sys

input = sys.stdin.readline

N = int(input())
answer = 0
queue = PriorityQueue()

for _ in range(N):
    queue.put(int(input()))

for _ in range(N - 1):
    temp = 0
    temp += queue.get()
    temp += queue.get()
    answer += temp
    queue.put(temp)

print(answer)
