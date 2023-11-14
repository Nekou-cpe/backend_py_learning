'''seter getter second model
first you should write getter method by decoder @property
then you should write setter method by decoder @nameOfPriviteValue.setter 
point: plus self you should add name of value in setter
use value name withou __
we use getter and setter for access to privite value with security'''
class Person():
    def __init__(self,name,idCode) -> None:
        self.name=name
        self.__idCode=idCode

    @property
    def idCode(self):
        return self.__idCode
    
    @idCode.setter 
    def idCode(self,idCode):
        self.__idCode=idCode
    

Person1=Person('Nekou','400130100')
print(Person1.idCode)