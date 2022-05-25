def prime(ini,fi):
    s=0
    for i in range(ini,fi+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            s+=i

    return s



initial=int(input('enter initial range '))
final=int(input('enter final range '))
result=prime(initial,final)
print('sum= ',result)
print(prime(2,10))

