from collections import deque
import sys

input = sys.stdin.readline

stack_L = list(input().rstrip())
stack_R = []
N = int(input())

for i in range(N):
    command = input().split()

    if command[0] == "L" and stack_L:
        stack_R.append(stack_L.pop())
    elif command[0] == "D" and stack_R:
        stack_L.append(stack_R.pop())
    elif command[0] == "B" and stack_L:
        stack_L.pop()
    elif command[0] == "P":
        stack_L.append(command[1])

stack_L.extend(reversed(stack_R))
print("".join(stack_L))
