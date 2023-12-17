'''abstraction
    when you want to have a method insid all your children and call it inside 
    parent class but it does not work on classs
    it works just insid children class
    #ABC ->shows this parent class has abstract
    #abstractmethod -> this force to have abstract method all children '''
from abc import ABC,abstractmethod 
class Shapes(ABC):
    count_shapes=0
    lists=[]
    def __init__(self,type,color) -> None:
        Shapes.count_shapes+=1
        self.type=type
        self.color=color
    @abstractmethod
    def perimiter(self):#this is abestract
        pass
    
    @classmethod
    def list_Shapes(cls,name):
        Shapes.lists.append(name)
        return Shapes.lists

    def __repr__(self) -> str:
        return super().__repr__()
class Circle(Shapes):
    def __init__(self, type, color,diameter) -> None:
        super().__init__(type, color)
        self.diameter=diameter
    def perimiter(self):
        return self.diameter*self.diameter
    
class Rectangle(Shapes):
    def __init__(self, type, color,lenght,width) -> None:
        super().__init__(type, color)
        self.lenght=lenght
        self.width=width
    def perimiter(self):
        return self.lenght*2+self.width*2
    
class Squer(Shapes):
    def __init__(self, type, color,width) -> None:
        super().__init__(type, color)
        self.width=width

    def perimiter(self):
        return self.width*4
    
Squer1=Squer('sqr','red',2)
print(Squer1.perimiter())
Rectangle1=Rectangle('rectangle','black',12,10)
print(Rectangle1.perimiter())
Circle1=Circle('circle','blue',3)
Shapes.list_Shapes(Squer1)
Shapes.list_Shapes(Rectangle1)
Shapes.list_Shapes(Circle1)
print(Shapes.lists)