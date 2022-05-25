class Employment:
    company='Microsoft'
    def set_employees(self,name,id,designation,salary):
        self.n=name
        self.id=id
        self.d=designation
        self.s=salary

    def print_employees(self):
        print(self.n)
        print(self.id)
        print(self.d)
        print(self.s,'/-')
        print(Employment.company,'\n----------------')
e=Employment()
e.set_employees('vishnu',3432,'developer',30000)
e.print_employees()
e2=Employment()
e2.set_employees('abi',3433,'devloper',45000)
e2.print_employees()