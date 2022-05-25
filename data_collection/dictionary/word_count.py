s='hello hai hello hi hi hello ha'
d={}
a=s.split(' ')
# for i in a:
#     d[i]=a.count(i)
print(a)
for i in a:
    if i not in d:
        d[i]=1
    else:
        val=d[i]
        val+=1
        d.update({i:val})
        # d[i]=val
print(d)




