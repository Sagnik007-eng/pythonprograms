class Vehicle:
    color='red'
    vehicle_count=0
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type
        Vehicle.vehicle_count+=1
        print('brand is ',self.brand)
        print('type is ',self.type)
    def get_vehicle_count(self):
        return Vehicle.vehicle_count
    def drive(self):
        print('vehicle driving')

class Truck(Vehicle):
    #pass
    def drive(self):
        print('truck driving') # this is called overriding of method drive in derived class.
class Motorcycle(Vehicle):
    def drive(self):
        print('motorcycle driving')


"""v1=Vehicle('Tata','Punch')
v2=Vehicle('BMW','SUV')
v3=Vehicle('Skoda','Laura')
v4=Vehicle('Honda','Civic')
v5=Vehicle('Honda','Civic')
v6=Vehicle('Nissan','Micra')
v7=Vehicle('Hyundai','i20')
print(v1.type)
print(v1.color)"""

"""print(v2.type)
print(v2.color)
print('Num of vehicles',v6.get_vehicle_count())

t1=Truck('Tata','t15')
t2=Truck('Mercedes','m15')
print('Num of vehicles',t2.get_vehicle_count())
t2.drive()
m1=Motorcycle('BMW','b1')
print('Num of vehicles',m1.get_vehicle_count())
m1.drive()
for v in [v1,t1,m1]:
    v.drive()   #this is called polymorphism. Same drive method taking many forms.

print(type(m1))"""
