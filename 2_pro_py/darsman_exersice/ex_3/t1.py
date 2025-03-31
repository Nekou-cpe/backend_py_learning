''''''
class Programming_Language_Course():
    def __init__(self,code_corse,dedline,level,pay,teacher) -> None:
        self.code_corse=code_corse
        self.dedline=dedline
        self.level=level
        self.pay=pay
        self.teacher=teacher
        self.count_days=[]

    def add_Day(self,day):
        self.count_days.append(day)
        return self.count_days

    def __repr__(self) -> str:
        return f'{self.code_corse}\t{self.dedline}\t{self.level}\t{self.pay}\t{ self.teacher}\t{self.count_days}'
    
    def list_course(self):
        Programming_Language_Course.list_course.append(self.__repr__())

class Python(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher)
        self.count_days=[]

class Java(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher)
    
class PHP(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher)


#instances: 
Python1=Python(10,'1may-20jun','Basic',900020,'shkspier')
Python2=Python(10,'1may-20jun','Advanced',900020,'shkspier')
Python1.add_Day('monday')

Java1=Java(10,'1may-20jun','Basic',900020,'shkspier')
Java2=Java(10,'1may-20jun','Advanced',900020,'shkspier')

PHP1=PHP(10,'1may-20jun','Basic',900020,'shkspier')
PHP2=PHP(10,'1may-20jun','Advanced',900020,'shkspier')

list_courses=[Python1,Python2,PHP1,PHP2,Java1,Java2]
print(f'code \tdedline \tlevel \tpay \teacher \tdays')
for i in list_courses:
    print(i)