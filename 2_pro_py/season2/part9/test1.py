'''__eq__ model 1'''
class Student():
    def __init__(self,name,age,idCode) -> None:
        self.name=name
        self.age=age
        self.idCode=idCode

    def __str__(self) -> str:
        return f'{self.name}{self.age}{self.idCode}'
        
    def __eq__(self, object) -> bool:
        if self.idCode == object.idCode :
            return 'it is a student '
        else:
            return 'there are two students'
        
Student1=Student('Nekou',20,400130100)
Student2=Student('Nekou',20,400130100)
Student3=Student('Nikol',22,400130183)
print(Student1==Student2) 
print(Student1==Student3) 