import sys
from collections import deque

n = int(sys.stdin.readline())
dequeue = deque()

for i in range (n):
    command = sys.stdin.readline().split()
    order = command[0]
    if order =="push_front":
        val = command[1]
        dequeue.appendleft(val)
    elif order =="push_back":
        val = command[1]
        dequeue.append(val)
    elif order =="pop_front":
        if len(dequeue)==0:
            print(-1)
        else :
            print(dequeue.popleft())
    elif order =="pop_back":
        if len(dequeue)==0:
            print(-1)
        else :
            print(dequeue.pop())
    elif order =="size":
        print(len(dequeue))
    elif order=="empty":
        if len(dequeue)==0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(dequeue)==0:
            print(-1)
        else:
            print(dequeue[0])
    elif order == "back":
        if len(dequeue)==0:
            print(-1)
        else:
            print(dequeue[-1])