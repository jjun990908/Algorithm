from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = 1
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s_arr = sorted(arr)
    bound = s_arr[0][1]
    for i in range(1, N):
        if s_arr[i][1] < bound:
            answer += 1
            bound = s_arr[i][1]
    print(answer)
