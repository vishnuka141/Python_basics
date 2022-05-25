import re
rule='[A-Z][\w]{3,8}[A-Z]'
s='Aakg35604K'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')