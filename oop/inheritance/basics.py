# single inheritance
class A:#parent class or base or super class
    def printa(self,a):
        self.a=a
        print('inside A ',self.a)
class B(A):#child class or sub or derived class
    def printb(self,b):
        self.b=b
        print('inside B ',self.b)
b=B()
b.printb(10)
b.printa(20)

a=A()
a.printa(3)