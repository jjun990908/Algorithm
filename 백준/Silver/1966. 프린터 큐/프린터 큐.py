from collections import deque
import sys


def find_Max():
    temp = 0
    for i in range(0, len(arr)):
        temp = max(temp, arr[i])
    return temp


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    queue = deque()
    answer = 0
    M, N = map(int, input().split())
    for i in range(0, M):
        queue.append(i)
    arr = list(map(int, input().split()))
    while 1:
        first = find_Max()
        popped = queue.popleft()
        if arr[popped] == first:
            answer += 1
            if popped == N:
                break
            else:
                arr[popped] = -1
        else:
            queue.append(popped)

    print(answer)
