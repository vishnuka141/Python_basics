l=[3,5,3,5,2,7,8,1,5,2,1,2]
d=[]
r=[]
for i in l:
    if i not in d:
        d.append(i)
    else:
        if i not in r:
            r.append(i)
print(r)
print('first recursive element: ',r[0],'\nlast recursive: ',r[-1])
