class Person:
    def p(self,name,age,place):
        self.n=name
        self.a=age
        self.p=place
class Parent:
    def par(self,ph,address):
        self.ph=ph
        self.add=address
class employee(Person,Parent):
    def emp(self,id,des,salary):
        print('name:',self.n,'\nage:',self.a,'\nplace:',self.p,'\nph.no:',self.ph,'\nadress:',self.add,'\nid:',id,'\ndesignation:',des,'\nsalary:',salary)
em=employee()
em.p('vishnu',34,'kochi')
em.par(123455,'kattukaran house')
em.emp(24564,'developer',25000)