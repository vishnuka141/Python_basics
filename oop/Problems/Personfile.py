class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Person name is ',self.name)
        print('Person age is ',self.age)
f=open('person','r')
for i in f:
    data=i.rstrip('\n').split(',')
    name=data[0]
    age=data[1]
    p=Person(name,age)