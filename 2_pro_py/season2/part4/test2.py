'''inheritance
2)multiple
point: order of prents is importent
for calling parents you should call them by names'''
class Mammal():
    def __init__(self,name,type) -> None:
        self.name=name 
        self.type=type
        print('init of Mammal')

    def __str__(self) -> str:
        return f'name {self.name},type {self.type}'

class WingedAnimal():
    def __init__(self,wing_count) -> None:
        self.wing_count=wing_count
        print('init of WingedAnimal')

    def __str__(self) -> str:
        return f'wing counts {self.wing_count}'

class Bat(Mammal,WingedAnimal):
    def __init__(self, name, type,wing_count,typeOfBat) -> None:
        Mammal.__init__(self,name, type)
        WingedAnimal.__init__(self,wing_count)
        self.typeOfBat=typeOfBat
        print('init of Bat')

    def __str__(self) -> str:
        return f'{Mammal.__str__(self)},{WingedAnimal.__str__(self)},type of Bat is {self.typeOfBat}'

Bat1=Bat('bat1','bat',2,'bat1')
print(Bat1)