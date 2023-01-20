import math
testcases = int(input())
for _ in range(testcases):
    H, W, N = map(int,input().split())
    end = math.ceil(N / H)
    first = N % H
    if(first ==0):
        first = H
    if(end < 10):
        print(first, end="")
        print(0, end="")
        print(end)
    else:
        print(first,end="")
        print(end)
