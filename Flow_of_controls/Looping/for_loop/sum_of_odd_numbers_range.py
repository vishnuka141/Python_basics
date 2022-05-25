initial = int(input('enter initial range '))
final = int(input('enter final range '))
sum=0
for i in range(initial,final+1):
    if i%2==1:
        sum+=i
print(sum)

for i in range(5,0,-1):
    print(i)