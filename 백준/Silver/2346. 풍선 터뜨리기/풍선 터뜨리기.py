from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
queue = deque(enumerate(map(int, input().split())))
answer = []

while queue:
    idx, paper = queue.popleft()
    answer.append(idx + 1)

    if paper > 0:
        queue.rotate(-(paper - 1))
    elif paper < 0:
        queue.rotate(-paper)

print(" ".join(map(str, answer)))
