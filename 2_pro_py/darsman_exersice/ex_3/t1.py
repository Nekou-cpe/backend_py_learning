''''''
class Programming_Language_Course():
    def __init__(self,code_corse,dedline,level,pay,teacher,count_days) -> None:
        self.code_corse=code_corse
        self.dedline=dedline
        self.level=level
        self.pay=pay
        self.teacher=teacher
        self.count_days=count_days

    def add_Day(self,day):
        pass

    def __repr__(self) -> str:
        return f'{self.code_corse},{self.dedline},{self.level},{self.pay},{ self.teacher},{self.count_days}'
    
    def list_course(self):
        Programming_Language_Course.list_course.append(self.__repr__())

class Python(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher, count_days) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher, count_days)
        self.count_days=[]
        super.add_Day()
    def __repr__(self) -> str:
        return super().__repr__()

class Java(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher, count_days) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher, count_days)

    def __repr__(self) -> str:
        return super().__repr__()
    
class PHP(Programming_Language_Course):
    def __init__(self, code_corse, dedline, level, pay, teacher, count_days) -> None:
        super().__init__(code_corse, dedline, level, pay, teacher, count_days)

    def __repr__(self) -> str:
        return super().__repr__()
    
#instances: 
Python1=Python(10,'1may-20jun','Basic',900020,'shkspier',['sunday','monday'])
Python2=Python(10,'1may-20jun','Advanced',900020,'shkspier',['sunday','monday'])

Java1=Java(10,'1may-20jun','Basic',900020,'shkspier',['sunday','monday'])
Java2=Java(10,'1may-20jun','Advanced',900020,'shkspier',['sunday','monday'])

PHP1=PHP(10,'1may-20jun','Basic',900020,'shkspier',['sunday','monday'])
PHP2=PHP(10,'1may-20jun','Advanced',900020,'shkspier',['sunday','monday'])

list_courses=[Python1,Python2,PHP1,PHP2,Java1,Java2]
print(list_courses)