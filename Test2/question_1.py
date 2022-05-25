class Vehicle:
    def printvehicle(self,type):
        self.type=type
class Bus(Vehicle):
    def details(self,veh_no,model):
        self.veh_no=veh_no
        self.model=model
        print(self.type,self.veh_no,self.model)
obj=Bus()
obj.printvehicle('Bus')
obj.details('Kl07 23423','TATA')