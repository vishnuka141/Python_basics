f=open('file.txt','r')
for i in f:
    s=i.rstrip('\n')
    print(s)