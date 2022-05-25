s1='loop'
s2='pool'
s1=s1.lower()
s2=s2.lower()
sort_s1=sorted(s1)
sort_s2=sorted(s2)
if sort_s1==sort_s2:
    print('the stings are anagram')
else:
    print('not anagram')

