class Pet:
    def __init__(self, name):
        self.n = name
class Cat(Pet):
    def __init__(self,domestic,color,name):
        super().__init__(name)
        self.d=domestic
        self.c=color
        print(self.n,'is a',self.d,'animal')
        print('Its',self.c,'color')
obj=Cat('domestic','white','cat')
