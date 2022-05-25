import re
s=input('enter ')
rule='[a-zA-Z][\w\W]{8}[\d]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')