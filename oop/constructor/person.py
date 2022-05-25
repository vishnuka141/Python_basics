class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print_value(self):
        print(self.name,self.age,self.place)
p=Person('vishnu',33,'kochi')
p.print_value()

p1=Person('akhil',34,'kaloor')
p1.print_value()