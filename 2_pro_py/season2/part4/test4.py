'''inheritance
4)hiorachical:'''
class Father():
    name_class='Father'
    def __init__(self,fname,lname,indCode) -> None:
        self.fname=fname
        self.lname=lname
        self.indCode=indCode
        print('this is init of Father')

    def __str__(self) -> str:
        return f'first name {self.fname},last name {self.lname},id code {self.indCode} '

class Son(Father):
    def __init__(self,fname,lname,indCode,age) -> None:
        Father.__init__(self,fname,lname,indCode)
        self.age=age
        print('this is init of son')

    def __str__(self) -> str:
        return f'{Father.__str__(self)}, age:{self.age}'
    
class Daughter(Father):
    def __init__(self, fname, lname, indCode,about) -> None:
        Father.__init__(self,fname, lname, indCode)
        self.about=about

    def __str__(self) -> str:
        return f'{Father.__str__(self)},about:{self.about}'
    
    
Daughter1=Daughter('Nekou','Dfrm',945,'female')
print(Daughter1)
son1=Son('Nikol','Dfrm',945,23)
print(son1)
