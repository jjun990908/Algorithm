from collections import deque

N, M = map(int, input().split())
target = list(map(int, input().split()))
queue = deque()
for i in range(1, N + 1):
    queue.append(i)

answer = 0
for i in target:
    while 1:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    answer += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    answer += 1

print(answer)
