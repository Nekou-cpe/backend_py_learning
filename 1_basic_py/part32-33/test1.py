'''inheritance -> you should create English school persons '''
'''polymorfice'''
class Person():
    person_count=0
    def __init__(self,fname,lname,age,id_code,about,) -> None:
        self.fname=fname
        self.lname=lname
        self.age=age
        self.id_code=id_code
        self.about=about
        Person.person_count+=1

    def __str__(self) -> str:
        return f'first name : {self.fname}\nlast name : {self.lname}\nage : {self.age}\nid : {self.id_code}\nabout : {self.about} {Person.person_count}\n'

    def showinfo(self):
        print(self.id_code)
class Student(Person):
    def __init__(self,fname,lname,age,id_code,about,student_number,languege) -> None:
        super().__init__(fname,lname,age,id_code,about)
        self.student_number=student_number
        self.languege=languege

    def showinfo(self): #polymorfice (this function is same as parent but change things inside )
        print(self.student_number)
    def __str__(self) -> str:
        return super().__str__() + f'student indentify : {self.student_number} \nlanguege : {self.languege}'


class Teacher(Person):
    def __init__(self,fname,lname,age,id_code,about,Teacher_number,languege) -> None:
        super().__init__(fname,lname,age,id_code,about)
        self.Teacher_number=Teacher_number
        self.languege=languege

    def __str__(self) -> str:
        return super().__str__()+f'Teacher code : {self.Teacher_number}\nlanguege : {self.languege}'
    
class Manager(Person):
    def __init__(self,fname,lname,age,id_code,about) -> None:
        super().__init__(fname,lname,age,id_code,about)

    def __str__(self) -> str:
        return super().__str__()
    
class Supporter(Person):
    def __init__(self,fname,lname,age,id_code,about,tag) -> None:
        super().__init__(fname,lname,age,id_code,about)
        self.tag=tag

    def __str__(self) -> str:
        return super().__str__()+f'supporter works : {self.tag}'
    
Student1=Student('Nekou','Dfrm',20,98328,'she is student of computer',12,'English')
print(Student1)