import re
s=input('enter number')
rule='[1][\w\W]{4}[0]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')