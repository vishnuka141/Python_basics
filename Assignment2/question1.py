class Employee:
    def __init__(self, name, salary, project):
        self.__name = name
        self.salary = salary
        self.project = project

    def show(self):
        print("Name: ", self.__name, 'Salary:', self.salary)
    def work(self):
        print(self.__name, 'is working on', self.project)


emp = Employee('Jessa', 8000, 'NLP')

emp.show()
emp.work()
print(emp.__name)