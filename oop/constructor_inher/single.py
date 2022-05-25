class A:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print(self.name,self.age,self.place)

class B(A):
    def __init__(self,roll,dep,name,age,place):
        super().__init__(name,age,place)
        self.roll=roll
        self.dep=dep
        print(self.roll,name,self.dep)

obj=B(1,'EC','vishnu',34,'kochi')
