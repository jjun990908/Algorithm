N = int(input())
a,b,c,d,e,f = map(int,input().split())

one = min(a,b,c,d,e,f)
two = min(a+b,a+c,a+d,a+e,b+c,b+d,b+f,c+e,c+f,d+e,d+f,e+f)
three = min(a+b+c,a+b+d,a+d+e,a+c+e,f+b+d,f+b+c,f+e+d,f+e+c)

form_1 = (N-2)**2+4*(N-1)*(N-2)
form_2 = 4*(N-1)+4*(N-2)

if (N==1):
    answer = (a+b+c+d+e+f)-max(a,b,c,d,e,f)
else:
    answer = (one*form_1)+(two*form_2)+(three*4)

print (int(answer))
