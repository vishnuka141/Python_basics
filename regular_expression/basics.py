# regular_expression re
# package....pattern matching
# finditer
count=0
import re
matcher=re.finditer('ab','aaabccabaab')
for i in matcher:
    print(i.group())#to search the group
    print(i.start())#which index to start the group
    count+=1
print(count)