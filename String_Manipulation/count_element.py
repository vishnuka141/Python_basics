s = 'aabbdcc'
e= input('enter a character ')
count=0
for i in s:
    if e in i:
        count=count+1

print(e,'in ',count,' times')