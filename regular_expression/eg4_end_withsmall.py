import re
s=input('enter number')
rule='\D*[a-zA-Z]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')