import sys

input = sys.stdin.readline

N = int(input())
stack = []
answer = []
flag = False
cur = 1
for i in range(N):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = True
        break

if flag == False:
    for i in answer:
        print(i)
