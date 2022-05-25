num=int(input('enter a number '))
# flag=0
# for i in range(2,num):
#     if num%i==0:
#         flag=1
# if flag:
#     print('not a prime number')
# else:
#     print('prime number')

for i in range(2,num):
    if num%i==0:
        print('not a prime')
        break
else:
    print('Prime number')