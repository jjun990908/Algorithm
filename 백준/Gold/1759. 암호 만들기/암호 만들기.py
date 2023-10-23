from collections import deque
import sys

input = sys.stdin.readline


def dfs(depth, start, password):
    if depth == L:
        count = 0
        for i in password:
            if i in "aeiou":
                count += 1
        if count <= 0 or count >= L - 1:
            return
        print(password)
        return

    for i in range(start, C):
        dfs(depth + 1, i + 1, password + answer[i])


L, C = map(int, input().split())
answer = list(input().split())

answer.sort()
dfs(0, 0, "")
