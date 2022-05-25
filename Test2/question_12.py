import re
def valid(fun):
    def wrapper(ph_number):
        rule = '[+][9][1]\d{10}'
        matcher = re.fullmatch(rule, ph_number)
        if matcher is not None:
            return fun(ph_number)
        else:
            raise ('not valid')
    return wrapper
@valid
def change_number(ph_number):
    new_number=ph_number
    return new_number
print(change_number('+912839204834'))
