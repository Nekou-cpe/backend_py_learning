''''''
class Programming_Language_Course():
    list_of_courses=[]
    def __init__(self,code_corse,dedline,level,pay,teacher,days=[]) -> None:
        self.code_corse=code_corse
        self.dedline=dedline
        self.level=level
        self.pay=pay
        self.teacher=teacher
        self.days=days
    
    def __str__(self) -> str:
        return f'{self.code_corse},{self.dedline},{self.level},{self.pay},{ self.teacher},{self.days}'
    
    def list_course(self):
        Programming_Language_Course.list_course.append(self.__str__())

class Python(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher, days=[]) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher, days)

    def __str__(self) -> str:
        return super().__str__()

class Java(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher, days=[]) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher, days)

    def __str__(self) -> str:
        return super().__str__()
    
class PHP(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher, days=[]) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher, days)

    def __str__(self) -> str:
        return super().__str__()
    
#instances: 
Python1=Python(10,'1may-20jun','Basic',900020,'shkspier',['sunday','monday'])
Python2=Python(10,'1may-20jun','Advanced',900020,'shkspier',['sunday','monday'])

Java1=Java(10,'1may-20jun','Basic',900020,'shkspier',['sunday','monday'])
Java2=Java(10,'1may-20jun','Advanced',900020,'shkspier',['sunday','monday'])

PHP1=PHP(10,'1may-20jun','Basic',900020,'shkspier',['sunday','monday'])
PHP2=PHP(10,'1may-20jun','Advanced',900020,'shkspier',['sunday','monday'])

print(Programming_Language_Course.list_course())