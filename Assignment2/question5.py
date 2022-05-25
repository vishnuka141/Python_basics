class Employee:
    def emp(self,name,id,des,salary):
        self.n=name
        self.id=id
        self.d=des
        self.s=salary
        print(self.n,self.id,self.d,self.s)
obj=Employee()
obj.emp('Arun',1,'developer',45000)
obj1=Employee()
obj1.emp('Amal',2,'Testor',34000)
obj2=Employee()
obj2.emp('Alan',3,'developer',50000)
obj3=Employee()
obj3.emp('Anaga',4,'Testor',30000)
obj4=Employee()
obj4.emp('Maya',5,'developer',60000)
