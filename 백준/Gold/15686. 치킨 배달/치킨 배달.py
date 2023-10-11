from itertools import combinations
import sys

input = sys.stdin.readline

MAX = int(1e9)
N, M = map(int, input().split())
answer = MAX
board = []
house = []
chicken = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])

for case in combinations(chicken, M):
    temp = 0
    for home in house:
        distance = MAX
        for i in range(M):
            distance = min(
                distance, abs(home[0] - case[i][0]) + abs(home[1] - case[i][1])
            )
        temp += distance
    answer = min(answer, temp)

print(answer)
