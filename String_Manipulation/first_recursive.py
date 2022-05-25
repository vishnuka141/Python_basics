str=input('enter a string ')
n=' '
r=" "
for i in str:
    if i not in n:
        n=n+i
    else:
        r=r+i
        break
print('first recursive: ',r)
