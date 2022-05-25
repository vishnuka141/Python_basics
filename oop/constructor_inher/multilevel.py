class Person:
    def __init__(self,name,age,place):
        self.n=name
        self.a=age
        self.p=place
class Child(Person):
    def __init__(self,ph,add,name,age,place):
        super().__init__(name,age,place)
        self.ph=ph
        self.add=add
class Student(Child):
    def __init__(self,dep,college,ph,add,name,age,place):
        super().__init__(ph,add,name,age,place)
        self.dep=dep
        self.col=college
        print(self.n,self.a,self.p,'\n',self.ph,self.add,self.dep,self.col)

s=Student('developer','ihrd',4005303,'house','abi',32,'kochi')