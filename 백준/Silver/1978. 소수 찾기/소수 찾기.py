n = int(input())
num = map(int, input().split())
answer = 0
for n in num:
    error = 0
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                error += 1
        if error == 0:
            answer = answer + 1
print (answer)