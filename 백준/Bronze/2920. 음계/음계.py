N = list(map(int, input().split()))
 
if N == sorted(N):
    print('ascending')
elif N == sorted(N, reverse=True):
    print('descending')
else:
    print('mixed')