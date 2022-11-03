def recurFactorial(n):
    if n == 1:
        return 1
    else:
        return n * recurFactorial(n-1)


print(recurFactorial(9))
