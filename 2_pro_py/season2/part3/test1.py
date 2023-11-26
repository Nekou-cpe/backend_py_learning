'''Encapsulation:
Encapsulation is a mechanism of wrapping the data (variables) and code 
acting on the data (methods) together as a single unit. In encapsulation,
the variables of a class will be hidden from other classes,
and can be accessed only through the methods of their current class.'''
import random
class Digital():
    __idntify=None
    _=None
    z=None
    def __init__(self,name,type,brand,idCode) -> None:
        self.name=name
        self.type=type
        self.brand=brand
        self.__idCode=idCode
    
    def __setidcod(self,__idcod):
        self.__idCode='@'+self.__idCode

    def __getidcod(self):
        return self.__idCode
    
    def __setIdnty(self,__idntify):
        self.__idntify=random.randint(1,8000)

    def __getIdnty(self):
        return self.__idntify
    
    def _showInfo(self):
        return f'name:{self.name},type: {self.type},brand: {self.brand}'
    

class Mobile(Digital):
    def __init__(self, name, type, brand, idCode,color,size) -> None:
        super().__init__(name, type, brand, idCode)
        self.color=color
        self.size=size

    def showinfo(self):
        return f'{self._showInfo()},color:{self.color}'
    
Digital1=Digital('tv','tv','something',987)
Mobile1=Mobile('mobile','mobile','sonmething else',76,'black','13')
print(Digital1._showInfo()) #you can not call protected method in instance same this
print(Mobile1.showinfo())