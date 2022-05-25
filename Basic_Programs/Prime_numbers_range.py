initial=int(input('enter initial range '))
final=int(input('enter final range '))
for i in range(initial,final+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)




