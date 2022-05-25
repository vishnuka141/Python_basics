class Person:
    def p(self,name,age,place):
        self.n=name
        self.a=age
        self.p=place
class Child(Person):
    def c(self,name,age):
        self.name=name
        self.age=age
class Student(Child):
    def S(self,dep,college):
        self.dep=dep
        self.col=college
        print(self.n,self.a,self.p,'\n',self.name,self.age,self.dep,self.col)
st=Student()
st.p('vishnu',56,'kochi')
st.c('venu',22)
st.S('electronics','IHRD')