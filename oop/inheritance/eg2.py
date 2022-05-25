class Person:
    def p(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
        print(self.name, self.age, self.place)
class Employment(Person):
    def set_employees(self,id,designation,salary):
        self.id=id
        self.d=designation
        self.s=salary
        print(self.id,self.name,self.d,self.s)
obj=Employment()
obj.p('vishnu',32,'kochi')
obj.set_employees(2134,'developer',2500)