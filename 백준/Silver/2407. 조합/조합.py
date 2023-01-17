def factorial(n):
    if (n>1):
        return n*factorial(n-1)

    else:
        return 1


a, b = map(int, input().split())
print(int(factorial(a)//(factorial(b)*factorial(a-b))))
