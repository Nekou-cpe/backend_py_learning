'''__eq__ model 2'''
class Student():
    def __init__(self,name,age,idCode) -> None:
        self.name=name
        self.age=age
        self.idCode=idCode

    def __str__(self) -> str:
        return f'{self.name}{self.age}{self.idCode}'
        
    def __eq__(self, object) -> bool:
        if not isinstance(object,self):
            return 'they are student and teacher'
        elif  self.idCode == object.idCode :
            return 'it is a student '
        else:
            return 'they are two students'
class Teacher():
    def __init__(self,name,age,idCode_t) -> None:
        self.name=name
        self.age=age
        self.idCode_t=idCode_t

    def __str__(self) -> str:
        return f'{self.name}{self.age}{self.idCode_t}'
    
Student1=Student('Nekou',20,400130100)
Student2=Student('Nekou',20,400130100)
Student3=Student('Nikol',22,400130183)
print(Student1==Student2) 
print(Student1==Student3) 
Teacher1=Teacher('MssNekou',90,2178)
print(Student3==Teacher1)