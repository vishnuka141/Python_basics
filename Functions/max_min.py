# def max_min():
#     n1=int(input('enter 2 numbers '))
#     n2=int(input())
#     if n1>n2:
#         print(n1,' is greater')
#     else:
#         print(n2,' is greater')
# max_min()

# def max_min(n1,n2):
#     if n1>n2:
#         print(n1,' is greater')
#     else:
#         print(n2,' is greater')
#
# n1=int(input('enter 2 numbers '))
# n2=int(input())
# max_min(n1,n2)

def max_min(n1,n2):
    greater=' is greater'
    if n1>n2:
        return str(n1)+greater
    elif n1==n2:
        return 'same values'
    else:
        return str(n2)+greater

n1=int(input('enter 2 numbers '))
n2=int(input())
result=max_min(n1,n2)
print(result)