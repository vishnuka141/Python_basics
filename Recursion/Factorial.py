def rec_factorial(n):
    if n==1:
        return  1
    else:
        return  n*rec_factorial(n-1)
print(rec_factorial(4))
