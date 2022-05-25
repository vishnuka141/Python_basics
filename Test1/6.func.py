def sum_odd(ini_,fin_):
    sum=0
    for i in range(ini_,fin_):
        if i%2==1:
            sum+=i
    return sum
print(sum_odd(40,80))