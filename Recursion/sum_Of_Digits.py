def sumDigit(n):
    if(n == 0 ):
        return 0
    else:
        return int(n%10) + sumDigit(int(n/10))



print(sumDigit(1234))

