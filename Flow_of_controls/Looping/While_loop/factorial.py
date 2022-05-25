n= int(input('enter a number '))
# i=1
# mul=1
# while i<=n:
#     mul*=i
#     i+=1
# print(mul)
sum=0
i=1
while i<=n:
    if  i%2==0:
        sum+=i
    i+=1
print(sum)