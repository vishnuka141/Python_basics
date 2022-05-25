i = int(input('enter a range '))
f = int(input('enter a range '))
sum=0
while i<=f:
    if i%2==0:
        sum+=i
    i+=1
print(sum)