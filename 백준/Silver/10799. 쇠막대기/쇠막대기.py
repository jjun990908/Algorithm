a = input()
b = list(a)
stack =0
sum =0
for i in range(len(b)-1):
    if a[i] == "(":
        if a[i+1] == ")":
            sum += stack
        else:
            stack += 1
    if a[i] == ")":
        if a[i-1] == "(":
            pass
        else:
            stack -= 1
            sum += 1
sum +=1
print(sum)