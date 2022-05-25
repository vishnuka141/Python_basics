import re
s=input('enter number')
rule='[a][\w\W]{3,6}[b]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')