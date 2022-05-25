class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Details(Person):
    def person_details(self,ph,address):
        self.ph=ph
        self.address=address
        print(self.name,self.ph,self.address,self.place)
        print('----------------------------')
# single inheritance

class Employee(Details):
    def emp(self,id,designation,com_name):
        self.id=id
        self.des=designation
        self.com_name=com_name
        print(self.name,self.id,self.des,self.com_name)
        print('----------------------------')
# multilevel inheritance


class Student:
    def set_student(self,roll,dep,college):
        self.roll=roll
        self.dep=dep
        self.college=college
class Personstudent(Person,Student):
    def person_details_only(self):
        print(self.roll,self.name,self.dep,self.college)
        print('----------------------------')
#multiple inheritance


detail=Details()
detail.setvalue('vishnu',24,'kochi')
detail.person_details(78944893385,'abc House')#single inheritance

emplo=Employee()
emplo.setvalue('vishnu',24,'kochi')
emplo.person_details(78944893385,'abc House')
emplo.emp(123,'developer','Microsoft')#multilevel inheritance

ps=Personstudent()
ps.setvalue('vishnu',24,'kochi')
ps.set_student(1,'CS','SH college')
ps.person_details_only()#multiple inheritance
