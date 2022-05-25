# x='a+' a including group
# count=0
# import re
# rule='[ab]+'
# matcher=re.finditer(rule,'aa bba acaa @12')
# for i in matcher:
#     print(i.group())#to search the group
#     print(i.start())#which index to start the group
#     count+=1
# print(count)

# x='a*' count including zero number of a
count=0
import re
rule='a*'
matcher=re.finditer(rule,'aa bba acaa @12')
for i in matcher:
    print(i.group())#to search the group
    print(i.start())#which index to start the group
    count+=1
print(count)

# x='a?' count a as each including zero no of a
count=0
import re
rule='a?'
matcher=re.finditer(rule,'aa bba acaa @12')
for i in matcher:
    print(i.group())#to search the group
    print(i.start())#which index to start the group
    count+=1
print(count)

# x='a{2} 2 no of a position(consider 2)
# count=0
# import re
# rule='a{2}'
# matcher=re.finditer(rule,'aa bba aacaa @12')
# for i in matcher:
#     print(i.group())#to search the group
#     print(i.start())#which index to start the group
#     count+=1
# print(count)

# x='a{2,3}' minimum 2 a and maximum 3 a
# count=0
# import re
# rule='a{2,3}'
# matcher=re.finditer(rule,'aa bba aaaa @12')
# for i in matcher:
#     print(i.group())#to search the group
#     print(i.start())#which index to start the group
#     count+=1
# print(count)

# x='^a' check starting with a
#'a$' ending with a
# count=0
# import re
# rule='a$'
# matcher=re.finditer(rule,'bab bba aaaa @12a')
# for i in matcher:
#     print(i.group())#to search the group
#     print(i.start())#which index to start the group
#     count+=1
# print(count)

