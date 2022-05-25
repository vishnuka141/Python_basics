l=[32,5,2,65,1,7,8,54,11,34]
def linear():
    e = int(input('enter element to search '))
    for i in l:
        if i ==e:
            print('found')
            break
    else:
        print('not found')

linear()