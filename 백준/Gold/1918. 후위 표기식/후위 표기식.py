import sys

input = sys.stdin.readline
str = list(input())
stack = []
answer = ""
for s in str:
    if s.isalpha():
        answer += s
    else:
        if s == "(":
            stack.append(s)
        elif s == "*" or s == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(s)
        elif s == "+" or s == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(s)
        elif s == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
while stack:
    answer += stack.pop()
print(answer)
