import re
s=input('enter ')
rule='[a-zA-Z]{5}'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')