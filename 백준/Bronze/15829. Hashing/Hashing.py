L = int(input())
string = input()
answer = 0

for i in range(L):
    answer += (ord(string[i]) - 96) * (31**i)
print(answer % 1234567891)
