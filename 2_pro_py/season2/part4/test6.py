import enum

class Alive():
    def __init__(self,name,code):
        self.name=name
        self._code = code

    def __repr__(self):
        return f'name : {self.name}'

class Animal(Alive):
    def __init__(self,name,code):
        Alive.__init__(self,name,code)

class Dog(Animal):
    def __init__(self,name,code,color):
        Animal.__init__(self,name,code)
        self.color=color

    def __repr__(self):
        return f'name : {self.name} color : {self.color}'

class ColorsCode(enum.Enum):
    Black=1
    White=2
    Brown=3
    Yellow=4

dog1=Dog('Chico',1234,ColorsCode.Black.value)
print(dog1)