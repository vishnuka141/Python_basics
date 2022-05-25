# def fact(n):
#     s=1
#     for i  in range(1,n+1):
#         s=s*i
#      print(s)
# num=int(input('enter a number '))
# fact(num)

def fact(n):
    s=1
    for i  in range(1,n+1):
        s=s*i
    return s
num=int(input('enter a number '))
print(fact(num))

