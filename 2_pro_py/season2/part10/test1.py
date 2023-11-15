'''__hash__
you should write four instance always inside your class'''
class Person():
    def __init__(self,fname,lname,id) -> None:
        self.fname=fname
        self.lname=lname
        self.__id=id
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id=id

    def __str__(self) -> str:
        return f'{self.fname},{self.lname},{self.__id}'

    def __hash__(self) -> int:
        return hash(self.__id)

    def __eq__(self, object) -> bool:
        if self.__id == object.__id:
            return 'this is a person'
        else:
            return 'they are two deffrent persons'
        
Person1=Person('Nekou','Dfrm',400130100)
Person2=Person('Nikol','Mrfd',400130183)
print(Person1==Person2)
sett={Person2,Person2,Person1} #set works with hash so when you work on objects set you should return the hash in set
print(sett)
