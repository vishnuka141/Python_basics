def vacc(fun):
    def wrapper(name,age):
        if age>=18:
            return fun(name,age)
        else:
            raise Exception('not allowed')
    return wrapper
@vacc
def vaccinate(name,age):
    return 'vaccinated'

print(vaccinate('vishnu',23))