import re
rule='[A-Z][a-z\W]+'
s='Akdj%#fk'
matcher=re.fullmatch(rule,s)

if matcher is not None:
    print('correct sequence')
else:
    print('invalid sequence')