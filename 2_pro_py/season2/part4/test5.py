'''inheritance
5)hybrid:'''
class Animal():
    def __init__(self,nameOfAnimal) -> None:
        self.nameOfAnimal=nameOfAnimal

    def __str__(self) -> str:
        return f'name of animal : {self.nameOfAnimal}'
        
class Mammal(Animal):
    def __init__(self,nameOfAnimal,name,type) -> None:
        Animal.__init__(self,nameOfAnimal)
        self.name=name 
        self.type=type
        print('init of Mammal')

    def __str__(self) -> str:
        return f'{Animal.__str__(self)}name {self.name},type {self.type}'

class WingedAnimal(Animal):
    def __init__(self,nameOfAnimal,wing_count) -> None:
        Animal.__init__(self,nameOfAnimal)
        self.wing_count=wing_count
        print('init of WingedAnimal')

    def __str__(self) -> str:
        return f'{Animal.__str__(self)}wing counts {self.wing_count}'

class Bat(Mammal,WingedAnimal):
    def __init__(self,nameOfAnimal,name, type,wing_count,typeOfBat) -> None:
        Mammal.__init__(self,name, type)
        WingedAnimal.__init__(self,wing_count)
        self.typeOfBat=typeOfBat
        print('init of Bat')

    def __str__(self) -> str:
        return f'{Mammal.__str__(self)},{WingedAnimal.__str__(self)},type of Bat is {self.typeOfBat}'

Bat1=Bat('bat','bat1','bat',2,'bat1')
print(Bat1)