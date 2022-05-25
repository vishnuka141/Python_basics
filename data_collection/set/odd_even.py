s={2,4,1,5,6,7,9,8,11,23,45,44,66,12}
odd=set()
even=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(even)
print(odd)