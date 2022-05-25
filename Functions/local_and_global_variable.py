a=32
def printa():
    global a,b#to declared as global variable using global keyword, scope outside the fuction when funciton worked.
    a=5      #if not declared as global its considered as local variable.
    b=6
    # print(a)

printa()
print(a)
print(b)