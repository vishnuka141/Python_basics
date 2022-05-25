# def printa(*args):
#     print(args)
# printa(3,5,6)

def add(*args):
    s=0
    for i in args:
        s=s+i
    # s=sum(args)
    print(s)
add(1,2,3,6)
