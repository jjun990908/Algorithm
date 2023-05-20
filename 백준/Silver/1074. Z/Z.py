N, R, C = map(int, input().split())
answer = 0

while(N!=0):
    # if (R < 2**(N-1) and C < 2**(N-1)): # //1사분면
    if (R < 2**(N-1) and 2**(N-1) <= C): # //2사분면
        C = C-2**(N-1)
        answer = answer + (((2**N)**2)/4)*1
    if (2**(N-1) <= R and C < 2**(N-1)): # //3사분면
        R = R- 2**(N-1)
        answer = answer + (((2**N)**2)/4)*2
    if (2**(N-1)<= R and 2**(N-1) <= C): # //4사분면
        R = R-2**(N-1)
        C = C-2**(N-1)
        answer = answer + (((2**N)**2)/4)*3
    N = N-1
print(int(answer))