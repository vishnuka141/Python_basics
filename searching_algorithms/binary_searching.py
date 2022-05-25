l=[2,1,3,7,4,6]
e=int(input('enter element to search '))
flag=0
l.sort()
low=0
upper=len(l)-1
while low<=upper:
    middle_index=(low+upper)//2
    if l[middle_index]==e:
        flag=1
        break
    elif e<l[middle_index]:
        upper=middle_index-1
    elif e>l[middle_index]:
        low=middle_index+1
if flag:
    print(e,'is present')
else:
    print(e, 'is not present')
