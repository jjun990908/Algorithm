n = input()
list = n.split()
x = int(list[0])
y = int(list[1])
w = int(list[2])
h = int(list[3])
a = w-x
b = h-y
if x <= y :
    if a <= x:
        if a <= b :
            print (a)
        else:
            print (b)
    elif b <= x :
        if a <= b :
            print (a)
        else:
            print (b)
    else :
        print(x)
elif y <= x :
    if a <= y:
        if a <= b :
            print (a)
        else:
            print (b)
    elif b <= y :
        if a <= b :
            print (a)
        else:
            print (b)
    else :
        print(y)