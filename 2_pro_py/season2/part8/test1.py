'''seter getter first model'''
class Person():
    def __init__(self,name,idCode) -> None:
        self.name=name
        self.__idCode=idCode

    def getIdCode(self):
        return self.__idCode
    
    def setIdCode(self):
        self.__idCode=self.__idCode


    

Person1=Person('Nekou','400130100')
print(Person1.getIdCode())