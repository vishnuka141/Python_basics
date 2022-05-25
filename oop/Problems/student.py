class Student:
    def __init__(self,roll,name,dep):
        self.roll=roll
        self.name=name
        self.dep=dep
        print(self.roll,self.name,self.dep)
f=open('student.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    roll=data[0]
    name=data[1]
    dep=data[2]
    st=Student(roll,name,dep)