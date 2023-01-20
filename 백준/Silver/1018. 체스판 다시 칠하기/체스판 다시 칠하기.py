N,M = map(int,input().split())
chess=[]
result=[]
for _ in range(N):
    chess.append(list(map(str,input())))
for i in range(0, N-7):
    for j in range(0, M-7):
        case_1 = 0
        case_2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if chess[x][y] != 'W':
                        case_1 += 1
                    if chess[x][y] != 'B':
                        case_2 += 1
                else:
                    if chess[x][y] != 'W':
                        case_2 += 1
                    if chess[x][y] != 'B':
                        case_1 += 1
        result.append(case_1)
        result.append(case_2)
print(min(result))