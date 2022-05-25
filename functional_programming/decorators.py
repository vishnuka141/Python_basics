def changevalue(fun):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return fun(a,b)
        else:
            fun(a,b)
    return wrapper
@changevalue
def sub(n1,n2):
    print(n1-n2)
sub(2,3)
@changevalue
def div(n1,n2):
    print(n1/n2)
div(5,10)
# vaccination decorator below 18 not vaccinated