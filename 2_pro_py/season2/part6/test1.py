'''polymorphism
2)overriding'''
class Vehicle():
    count_Vehicle=0
    def __init__(self,countV,type,brand) -> None:
        self.countV=countV
        self.type=type
        self.brand=brand
        Vehicle.count_Vehicle+=1
        print('this is init of Vehicle class')

    def show_info(self):
        print('this Show info vehicle class')
        return f'type:{self.type},brand:{self.brand},number of this {self.type} is {Vehicle.count_Vehicle}'

class Car(Vehicle):
    def __init__(self, countV, type, brand,model,years) -> None:
        Vehicle.__init__(self,countV, type, brand)
        self.model=model
        self.years=years
        print('this is init of car class')

    def show_info(self): #this is overriding
        print('this Show info Car class')
        return f'{Vehicle.show_info(self)},model of this car:{self.model},years works:{self.years}'
    
car1=Car(4,'car','BMW','5 series',2022)
print(car1.show_info())

