T = int(input())

for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    if N > 32:
        print(0)
    else:
        answer = 99999
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i == j or j == k or k == i:
                        pass
                    else:
                        temp = 0
                        for l in range(4):
                            if mbti[i][l] != mbti[j][l]:
                                temp += 1
                            if mbti[i][l] != mbti[k][l]:
                                temp += 1
                            if mbti[j][l] != mbti[k][l]:
                                temp += 1
                        answer = min(answer, temp)
        print(answer)
