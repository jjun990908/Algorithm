N = int(input())
arr = list(map(int, input().split()))
kidsNum = int(input())


def changeSwitch(index):
    if arr[index - 1]:
        arr[index - 1] = 0
    else:
        arr[index - 1] = 1


for _ in range(kidsNum):
    type, number = map(int, input().split())
    if type == 1:
        for i in range(N // number):
            changeSwitch(number * (i + 1))
    elif type == 2:
        confirm = 0
        temp = 0
        if number != 1 and number != N:
            while True:
                if arr[number - temp - 1] == arr[number + temp - 1]:
                    confirm = temp
                    temp += 1
                else:
                    break
                if (number - temp) == 1 or (number + temp) == N:
                    break
            if arr[number - temp - 1] == arr[number + temp - 1]:
                confirm = temp

        index = number - confirm
        for _ in range(2 * confirm + 1):
            changeSwitch(index)
            index += 1

divide = N // 20

for i in arr:
    print(i)
