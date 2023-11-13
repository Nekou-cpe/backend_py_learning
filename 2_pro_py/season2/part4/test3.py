'''inheritance
3)multi level:'''
class Parallelogram():
    def __init__(self,diameter) -> None:
        self.diameter=diameter
        print('this is init of Parallelogram')

    def __str__(self) -> str:
        return f'this is Parallelogram ,diameter:{self.diameter}'
class Rectangle(Parallelogram):
    def __init__(self, diameter,len1,len2) -> None:
        Parallelogram.__init__(self,diameter)
        self.len1=len1
        self.len2=len2
        print('this is init of Rectangle')

    def __str__(self) -> str:
        return f'{Parallelogram.__str__(self)},len1 : {self.len1},len2 : {self.len2}'
    
class Squer(Rectangle):
    def __init__(self, diameter,len1,len2,area):
        Rectangle.__init__(self,diameter,len1,len2)
        self.area=area
        print('this is init of squer')

    def __str__(self) -> str:
        return f'{Parallelogram.__str__(self)},{Rectangle.__str__(self)},area : {self.area}'

Rectangle1=Rectangle(10,12,3)
print(Rectangle1)
Squer1=Squer(9,7,7,28)
print(Squer1)