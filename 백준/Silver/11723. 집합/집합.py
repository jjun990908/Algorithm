import sys
from collections import deque

n = int(sys.stdin.readline())
S = list()

for i in range (n):
    command = sys.stdin.readline().split()
    order = command[0]
    if order =="add":
        val = command[1]
        if(val not in S):
            S.append(val)
    elif order =="remove":
        val = command[1]
        if(val in S):
            S.remove(val)
    elif order =="check":
        val = command[1]
        if(val in S):
            print(1)
        else:
            print(0)
    elif order=="toggle":
        val = command[1]
        if(val in S):
            S.remove(val)
        else:
            S.append(val)
    elif order == "all":
        S = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    elif order == "empty":
        S = []
    # elif order =="print":
    #     print(S)