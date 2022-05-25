s={3,5,-5,6,-2,-7,1,9,-8,-33,-43,32,43,2}
pos=set()
neg=set()
for i in s:
    if i>0:
        pos.add(i)
    else:
        neg.add(i)
print(pos)

print(neg)