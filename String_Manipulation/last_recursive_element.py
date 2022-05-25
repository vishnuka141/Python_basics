s=input('enter a string ')
r=" "
n=" "
for i in s:
    if i not in r:
        r=r+i
    else:
        n=n+i
print(n)
print(n[-1])
