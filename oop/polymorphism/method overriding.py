class A:
    def printa(self,n1):
        self.n1=n1
        print('inside A',self.n1)
class B(A):
    def printa(self,num1):
        self.num1=num1
        print('inside B',self.num1)

obj=B()
obj.printa(2)