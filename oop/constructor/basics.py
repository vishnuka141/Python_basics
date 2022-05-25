#to initialize instant variable while creating object.

class Add:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def addition(self):
        print('sum=',self.n1+self.n2)
num1 = int(input('enter 2 numbers\n'))
num2 = int(input())
a=Add(num1,num2)
a.addition()