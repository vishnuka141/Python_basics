class Book_a:
    def book_name(self,name):
        self.name=name
        print('booka name is ',self.name)
class Book_b(Book_a):
    def book_name(self,name):
        self.n=name
        print('Bookb name is ',self.n)
        super().book_name('Dc books')
obj=Book_b()
obj.book_name('wings of fire')