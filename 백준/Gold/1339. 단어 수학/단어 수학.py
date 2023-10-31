import sys

input = sys.stdin.readline

N = int(input())
words = []
value = {}
answer = 0
for _ in range(N):
    words.append(list(input().rstrip()))

for word in words:
    for index, id in enumerate(word):
        if id not in value:
            value[id] = 10 ** (len(word) - index - 1)
        else:
            value[id] += 10 ** (len(word) - index - 1)

value = sorted(value.items(), key=lambda x: x[1], reverse=True)
point = 9
valueNum = {}
for item in value:
    valueNum[item[0]] = point
    point -= 1

for word in words:
    temp = ""
    for i in word:
        temp += str(valueNum[i])
    answer += int(temp)

print(answer)
