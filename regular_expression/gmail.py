import re
s=input('enter mail ')
rule='[a-z\d]+[@][g][m][a][i][l][.][c][o][m]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')