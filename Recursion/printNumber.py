def printfun(n):
    if n == 1:
        print(1)
        return
    else:
        print(n)
        printfun(n-1)

    print(n)


print(printfun(10))
