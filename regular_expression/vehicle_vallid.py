import re
s=input('enter number')
rule='[K][L]\d{2}[A-Z]{2}\d{3,4}'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')