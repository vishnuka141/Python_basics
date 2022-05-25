class Person:
    def p(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print(self.name,self.age,self.place)
class Student(Person):
    def s(self,roll,dep):
        self.roll=roll
        self.dep=dep
        print(self.name,self.age,self.place,self.roll,self.dep)
objs=Student()
objs.p('vishnu',25,'kochi')
objs.s(1,'CS')