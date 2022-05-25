class Person:
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
        print(self.name, self.age, self.place)
class Parent:
    def __init__(self,ph,address):
        self.ph=ph
        self.add=address
        print(self.name,self.ph,self.add)
class Employment(Person,Parent):
    def __init__(self, id, designation,name, age, place, salary,ph,address):
        Person.__init__(self, name, age, place)
        Parent.__init__(self,ph,address)
        self.id = id
        self.d = designation
        self.s = salary
        print(self.id,name, self.d, self.s)
em=Employment(234,'developer','abi',34,'kochi',35000,756958493,'kallor house')