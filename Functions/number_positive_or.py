# def positive():
#     num=int(input('enter a number '))
#     if num>0:
#         print(num,' is positve')
#     elif num<0:
#         print(num,' is negative')
#     else:
#         print('zero')
# positive()

# def positive(num):
#     if num>0:
#         print(num,' is positve')
#     elif num<0:
#         print(num,' is negative')
#     else:
#         print('zero')
# n=int(input('enter a number '))
# positive(n)

def positive(num):
    if num > 0:
        return ('positve')
    elif num<0:
        return('negative')
    else:
        return('zero')
n=int(input('enter a number '))
print(positive(n))