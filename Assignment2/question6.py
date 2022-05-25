import re
s=input('enter')
rule='[\d][\w\W]+[A-Z]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')

