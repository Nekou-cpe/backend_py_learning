'''first class: work on car oop'''

class Car():
    count_cars=0 #variable class
    def __init__(self,brand,color,price) -> None:
        self.brand=brand
        self.color=color
        self.price=price 
        Car.count_cars+=1 #how write variable class in functions
        self.speed=200
    
    def __str__(self) -> str:
        
        