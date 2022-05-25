class Person:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    def __str__(self):
        return self.name+str(self.age)+self.place
p=Person('abi',32,'kochi')
print(p)