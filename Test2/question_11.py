import re
rule='[a][\d]{5}[b]'
s='a56563b'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')