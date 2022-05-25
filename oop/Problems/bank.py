class Bank:
    bank_name = 'SBI'
    def create(self,name,acno,min):
        self.name=name
        self.acno=acno
        self.min=min
        print(self.name,self.acno)
        print('min balance',self.min)
    def deposit(self,depos):
        self.depos=depos
        self.total=self.min+self.depos
        print('your',Bank.bank_name,'ac balance is ', self.total)
    def withdraw(self,w):
        self.w=w
        if self.w<self.total:
            print('balance=',self.total-self.w)
        else:
            print('insufficient balance')
b=Bank()
b.create('vishnu',123,1000)
b.deposit(1000)
b.withdraw(1000)
b.deposit(2000)
