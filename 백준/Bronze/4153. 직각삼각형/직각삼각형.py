while(1):
    a,b,c = map(int,input().split())
    if(a>b and a>c):
        if (a**2 == b**2 + c**2):
            print("right")
        else:
            print("wrong")
    elif(b>a and b>c):
        if (b**2 == a**2 + c**2):
            print("right")
        else:
            print("wrong")
    elif(c>b and c>a):
        if (c**2 == b**2 + a**2):
            print("right")
        else:
            print("wrong")
    else:
        break