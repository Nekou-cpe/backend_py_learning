class Person():
    def __init__(self,name,family,age,code):
        self.name=self.upperCase(name)
        self.family=self.upperCase(family)
        self.age=age
        self.__code=code

    def upperCase(self,strr):
        return strr.upper()

    def __repr__(self):
        return f'name : {self.name} code : {self.__code}'


person1=Person('Nekou','Dfrm',23,234)
print(person1)