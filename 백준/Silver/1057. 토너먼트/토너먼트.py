N, start, end = map(int, input().split())
answer = 0
while start != end:
    start -= start // 2
    end -= end // 2
    answer += 1
print(answer)
