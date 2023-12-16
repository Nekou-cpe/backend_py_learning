'''first class: work on car oop'''

class Car():
    count_cars=0 #variable class
    def __init__(self,brand,color,price) -> None:
        self.brand=brand
        self.color=color
        self.price=price 
        Car.count_cars+=1 #how write variable class in functions
        self.speed=200

    def __speed__(self,speed):
        print(f'the speed of this car is {self.speed}') 

    def __str__(self) -> str:
        return (f'about this car:name of brand :{self.brand} , color of this car :{self.color} , price :{self.price}')
        
print('count of cars: ',Car.count_cars)
car1=Car('Mvm X33','wite',478000000)
car2=Car('Aris','wite',900000000)
car3=Car('Tara','black',1000000)
car4=Car('Kfc','black',8000000)
car5=Car('Pjo','blue',78000000)
print(car1,'\n',car2,'\n',car3,'\n',car4,'\n',car5,'\n')
list_car=[car1,car2,car3,car4,car5]
print([car for car in list_car])
print('count of cars: ',Car.count_cars)