import re
f=open('phone.txt','r')
rule='[+][9][1]\d{10}'
for i in f:
    e=i.rstrip('\n')

    matcher=re.fullmatch(rule,e)
    num=matcher
    if matcher is not None:
        print(e)
