class Person:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
        print(self.name, self.age, self.place)
class Employment(Person):
    def __init__(self,id,designation,salary,name,age,place):
        super().__init__(name,age,place)
        self.id=id
        self.d=designation
        self.s=salary
        print(self.id,name,self.d,self.s)

em=Employment(123,'developer',23000,'vishnu',24,'kochi')