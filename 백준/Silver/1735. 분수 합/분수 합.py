def gcd(a,b):
    while a%b != 0:
        mod = a % b
        a = b
        b = mod
    return b

a, b = map(int, input().split())
c, d = map(int, input().split())
e = (a*d) + (c*b)
f = b*d
g = gcd(e,f)
print ((e//g),(f//g))
