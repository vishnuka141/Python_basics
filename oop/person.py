class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print_value(self):
        print(self.name,self.age,self.place)
p=Person()
p.setvalue('vishnu',33,'kochi')
p.print_value()

p1=Person()
p.setvalue('akhil',34,'kaloor')
p.print_value()
