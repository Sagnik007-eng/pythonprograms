import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod #decorator
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y


r=Rectangle(30,30)
print(r.area())

print(type(Shape))

print(type(Rectangle))