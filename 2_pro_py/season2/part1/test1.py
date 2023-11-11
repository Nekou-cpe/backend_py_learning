'''work with basic oop :
variable class and del def ->destroing object  init def ->creating object'''
class Animal():
    count=0 #static variable
    def __init__(self,name,type,age,about):
        self.name=name
        self.age=age
        self.type=type
        self.about=about
        Animal.count+=1
    def __str__(self) -> str:
        return f'type : {self.type} name: {self.name} age: {self.age} \n about this animal:{self.about} number of this animal is {Animal.count}'
    
    def __del__(self):
        print('deleted all object of Animal')
Animal1=Animal('mardi','dog',10,'it is a dog')
print(Animal1)
Animal2=Animal('kiten','cat',1,'it is a cat')
print(Animal2)
Animal3=Animal('red','fish',9,'it is a fish')
print(Animal3)
Animal4=Animal('rex','dog',7,'it is a dog')
print(Animal4)
print(Animal.count)
print(Animal2.count)
Animal2.count=10
print(Animal.count)
print(Animal2.count)
del(Animal4)
print(Animal4)