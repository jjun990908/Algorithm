import sys
from collections import deque

input = sys.stdin.readline


def cal(num, command):
    if command == "D":
        return (2 * num) % 10000
    if command == "S":
        return (num - 1) % 10000
    if command == "L":
        tmp = num // 1000
        return (num % 1000) * 10 + tmp
    if command == "R":
        tmp = num % 10
        return (num // 10) + (tmp * 1000)


def bfs(a, b):
    dcommand = ["D", "S", "L", "R"]
    queue = deque()
    queue.append([a, ""])
    while queue:
        num, str = queue.popleft()
        if num == b:
            print(str)
            break
        for i in range(4):
            new_num = cal(num, dcommand[i])
            if visited[new_num] == 0:
                visited[new_num] = 1
                queue.append([new_num, str + dcommand[i]])


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    visited[A] = 1
    bfs(A, B)
