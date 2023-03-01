n = int(input())
N = int(input())
answer = 0
for i in range (n,0,-1):
    a = (N//(10**(i-1)))
    answer = answer + a
    N = N - a*(10**(i-1))
print (answer)
