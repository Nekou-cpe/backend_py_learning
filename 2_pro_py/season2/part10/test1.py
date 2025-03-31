'''__hash__
you should write for instance always inside your class'''
class Person():
    def __init__(self,fname,lname,id) -> None:
        self.fname=fname
        self.lname=lname
        self.__id=id
    
    @property #getter
    def id(self):
        return self.__id
    @id.setter #setter
    def id(self,id):
        self.__id=id

    def __repr__(self) -> str:
        return f'{self.fname},{self.lname},{self.__id}'

    def __hash__(self) -> int:
        return hash(self.__id)+hash(self.fname)+hash(self.lname)

    def __eq__(self, object) -> bool:
        if self.__id == object.__id:
            return 'this is a person'
        else:
            return 'they are two deffrent persons'
        
Person1=Person('Nekou','Dfrm',400130100)
Person2=Person('Nikol','Mrfd',400130183)
Person3=Person('Nekou','Dfrm',400130100)
print(Person1==Person2)
sett={Person2,Person2,Person1,Person3} #set works with hash so when you work on objects set you should return the hash in set for dont repeat 
list_person=[Person3,Person2,Person1]
print(sett)
print(list_person)

