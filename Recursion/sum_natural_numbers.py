def sum_natural(n):
    if n==0:
        return n
    else:
        return n+sum_natural(n-1)
print(sum_natural(3))