import re
def check_mail(fun):
    def wrapper(mailid,password):
        rule = '[a-z\d]+[@][g][m][a][i][l][.][c][o][m]'
        matcher = re.fullmatch(rule, mailid)
        if matcher is not None:
            return fun(mailid,password)
        else:
            return 'invalid gmail'
    return wrapper


@check_mail
def login(mailid,password):
    return 'successfully completed login process'

print(login('vishnuka123@gmail.com','123455'))