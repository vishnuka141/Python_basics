class A:
    def printa(self):
        print('inside A')
class B(A):
    def printb(self):
        print('inside B')
class C(B):
    def printc(self):
        print('inside C')
objc=C()
objc.printa()
objc.printb()
objc.printc()