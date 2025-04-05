class Student():
    name_school=''
    def __init__(self,id,fname,lname,level):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.level=level

    @classmethod
    def school_name(Student,newName):
        Student.name_school=newName
        return Student.name_school
    
    @staticmethod
    def lessons(number_level):
        list_lessons = {  # Fixed assignment operator
            1: ['math', 'physic', 'chemistry'],
            2: ['math', 'physic', 'chemistry'],
            3: ['math', 'physic', 'chemistry'],
            4: ['math', 'physic', 'chemistry'],
            5: ['math', 'physic', 'chemistry'],
            6: ['math', 'physic', 'chemistry']
        }
        return list_lessons[number_level]

    def __hash__(self):
        return hash(self.id)

    def __eq__(self,obj):
        if self.id==obj.id:
            return 'same student'
        else:
            return 'two diffrent student'

    def __repr__(self):
        return f'id:{self.id},name:{self.fname , self.lname},level:{self.level}'

###############instance method
all_students=[]

std1=Student(324,'nekou','dfrm',2)
std2=Student(3,'nekou','dfrm',2)
std3=Student(324,'nekou','dfrm',2)
std4=Student(324,'nekou','dfrm',2)

all_students.append(std1)
all_students.append(std2)
all_students.append(std3)
all_students.append(std4)

for std in all_students:
    print(std)

print(std1.__eq__(std1))
print(std1.__eq__(std2))

print(Student.school_name('ABC'))
print(Student.lessons(1))