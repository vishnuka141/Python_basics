num1=int(input('enter 2 numbers\n'))
num2=int(input())
try:
    print('inside try')
    print(num1/num2)
# except:
#     print('exception occured')
except Exception as e:
    print('exception occurred',e)
finally:
    print('inside finally')# finally works all time