def pin(fun):
    def wrapper(name,pin):
        if name=='admin':
            return fun(name,pin)
        else:
            raise Exception('not allowed to change')
    return wrapper
@pin
def changepin(user_name,pin):
    mypin=pin
    return mypin
print(changepin('admi',345))
