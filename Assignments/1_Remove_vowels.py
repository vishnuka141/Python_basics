string=input('enter a word ')
new=''
for i in string:
    if i not in 'a,e,i,o,u':
        new+=i
print(new)
