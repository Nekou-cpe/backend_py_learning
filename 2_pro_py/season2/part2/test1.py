''' modifiers:
    __privite->using by just class
    public
    _protected-> using by class and child
    point: privite and protected can not use by instance'''

class Person():
    _name=None
    __id=None
    def __init__(self,id,name) -> None:
        self._name=name
        self.__id=id

    def _showName(self):
        return self._name
    
    def getId(self):
        return self.__id
    def setId(self,__id):
        self.__id=self.__id+1

#point it's better to do not call any protect or privat modifier from instance
class Student(Person):
    __idStudent=None
    def __init__(self,id,name,idStudent) -> None:
        super().__init__(id,name)
        self.__idStudent=idStudent

    def showname(self):
        self._showName

Student1=Student(1,'Nekou',654)