l=[2,5,1,6,9,3]
sor=[]
while l :
    min=l[0]
    for i in l:
        if i<min:
            min=i
    sor.append(min)
    l.remove(min)
print(sor)
print(l)
