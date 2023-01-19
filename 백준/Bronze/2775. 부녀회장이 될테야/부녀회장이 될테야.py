testcases = int(input())
for _ in range(testcases):
    a = int(input())
    b = int(input())
    house = [i for i in range(1,b+1)]

    for x in range(a):
        for y in range(1,b):
            house[y] += house[y-1]
    print(house[-1])