class Student:
    college='IHRD'#static value, call using class name.variable
    def set_value(self,name,roll_no,department):
        self.n=name
        self.r=roll_no
        self.d=department

    def print_value(self):
        print(self.n,self.r,self.d,Student.college)
s=Student()
s.set_value('vishnu',3,'EC')
s.print_value()

s1=Student()
s1.set_value('abi',1,"CS")
s1.print_value()