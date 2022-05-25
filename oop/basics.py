# object oriented programming
# class - a base model
# object- real word entity
# reference -store object ,operation
class Person:
    def read(self):
        print('person is reading')
    def write(self):
        print('person is writing ')
pe=Person()
pe.read()
pe.write()

pe2=Person()
pe.read()