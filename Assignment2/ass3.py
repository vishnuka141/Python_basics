class A:
    def __init__(self,a):
        self.a=a
        print('Its A class')
class B(A):
    def __init__(self,b,a):
        super().__init__(a)
        self.b=b
        print('Its B class')
    def fun(self):
        print(self.b)
class C(B):
    def __init__(self,c,b,a):
        super().__init__(b,a)
        self.c=c
        print('Its C class',self.b,self.a)
obj=C('Theater','Car','bus')
obj.fun()