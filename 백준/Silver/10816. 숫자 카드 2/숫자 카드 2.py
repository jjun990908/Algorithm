N = int(input())
cards = list(map(int,input().split()))
M = int(input())
find = list(map(int,input().split()))

dic = {}

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic [i] = 1

for i in find:
    if i in dic:
        print(dic[i],end=" ")
    else:
        print(0, end=" ")