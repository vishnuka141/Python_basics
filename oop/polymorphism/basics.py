# method overloading
#same method name and different no of arguments

class A:
    def printa(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1,self.n2)
class B(A):
    def printa(self,num1):
        self.num1=num1
        print(self.num1)
obj=B()
obj.printa(2,5)#python doesn't support overloading now.
