class Animal:
    def __init__(self,wild,domestic):
        self.wild=wild
        self.domestic=domestic
class Dog(Animal):
    def __init__(self,set,wild,domestic):
        super().__init__(wild,domestic)
        self.set=set
        print(set,'is a',self.domestic,'animal')
obj=Dog('Dog','wild','domestic')
