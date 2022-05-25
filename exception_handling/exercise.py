age=int(input('enter age '))
if age>=18:
    print('eligible for vaccine')
else:
    raise Exception('not eligible')