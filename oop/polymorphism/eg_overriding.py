class A:
    def printa(self,name):
        self.name=name
        print('its',self.name)
class B(A):
    def printa(self,name):
        self.n=name
        print(self.n)
obj=B()
obj.printa('vishnu')