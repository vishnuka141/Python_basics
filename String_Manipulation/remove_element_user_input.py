str=input('enter a string ')
remove= input('enter a element ')
r=" "
for i in str:
    if i not in remove:
        r=r+i

print(r)