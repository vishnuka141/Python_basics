# x='[abc]' either a,b or c
# x='[^abc]' except abc
# x='[a-z]' a to z
# x='[A-Z]' A to Z
# x='[a-zA-Z]' both lower and upper case are checked
# x='[0-9]' check digits
# x='[^a-zA-Z0-9]' special symbols
# x='\s' check space
# x='\d' check the digits
# x='\D' except digits
# x='\w' all excepts special characters
# x='\W' for special characters
count=0
import re
rule='\s'
matcher=re.finditer(rule,'34aWS@ acs')
for i in matcher:
    print(i.group())#to search the group
    print(i.start())#which index to start the group
    count+=1
print(count)

# quantifiers rules
# quantifiers
# x='a+' a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2} 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a' check starting with a
# x='a$' check ending with a