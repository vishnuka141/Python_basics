import re
# s=input('enter phone number ')
# rule='\d{10}'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invalid')

s=input('enter phone number ')
rule='[+][9][1]\d{10}'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')