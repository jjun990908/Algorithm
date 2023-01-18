import sys

n = int(sys.stdin.readline())
stack = []

for i in range (n):
    command = sys.stdin.readline().split()
    order = command[0]
    if order =="push":
        val = command[1]
        stack.append(val)
    elif order =="pop":
        if len(stack)==0:
            print(-1)
        else :
            print(stack.pop())
    elif order =="size":
        print(len(stack))
    elif order=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])