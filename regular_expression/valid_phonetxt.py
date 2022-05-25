import re
f=open('phone.txt','r')

rule='[+][9][1][\d]{10}'

for i in f:
    num=i.rstrip('\n')
    # print(num)
    matcher = re.fullmatch(rule, num)

    if matcher is not None:
        print(num)
    # else:
    #     print('invalid')



