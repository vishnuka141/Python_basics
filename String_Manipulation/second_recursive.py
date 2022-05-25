s=input('enter a string')#aaabbcc
n=""
r=''
for i in s:
    if i not in n:
        n=n+i
    elif i not in r:
        r=r+i
print(r[1])
print(r)
