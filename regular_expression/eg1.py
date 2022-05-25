import re
s=input('enter number')
rule='[a][\w\W]*[b]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')