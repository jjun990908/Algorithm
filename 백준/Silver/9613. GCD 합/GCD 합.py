import sys,math
input = sys.stdin.readline

def gcd(a,b):
    while(True):
        r = b % a
        if r == 0:
            return a
        b = a; a = r

for _ in range(int(input())):
    arr = list(map(int,input().split()))
    n,nums,r = arr[0],arr[1:],0
    
    for i in range(n-1):
        for j in range(i+1,n):
            r += gcd(nums[i],nums[j])
    print(r)