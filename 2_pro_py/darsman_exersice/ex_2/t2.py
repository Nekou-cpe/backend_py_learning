'''shows all Persons work on company'''
class Person():
    '''this class is parent of all person work on company'''
    person_count=0
    def __init__(self,fname,lname) -> None:
        if fname != fname.title() or lname != lname.title():
            self.fname=fname.title()
            self.lname=lname.title()
        else:
            self.fname=fname
            self.lname=lname
        Person.person_count+=1

    def __hash__(self) -> int:
        return hash(Person.person_count)

    def __repr__(self) -> str:
        return f'{self.fname},{self.lname},{Person.person_count}'

class Mangager(Person):
    '''this class is manager class. that shows everything about managers '''
    mangager_count=0
    def __init__(self, fname, lname ,id,income) -> None:
        super().__init__(fname, lname)
        self.id=id
        self.income=income
        Mangager.mangager_count+=1

    def __hash__(self) -> int:
        return hash(Mangager.mangager_count,super().__hash__())
    
    def __repr__(self) -> str:
        return f'about manager :{Person.__repr__(self)},{self.id},{self.income},{Mangager.mangager_count}'
    
class Employee(Person):
    '''this class is Employee class. that shows everything about Employees '''
    employee_count=0
    def __init__(self, fname, lname,id,rank) -> None:
        super().__init__(fname, lname)
        rank_list=['A','B','C','D']
        if rank in rank_list:
            self.rank=rank
            Employee.employee_count+=1
            self.id=id
        else:
            print('Error')

    def __hash__(self) -> int:
        return hash(Employee.employee_count,super().__hash__())
        
    def __repr__(self) -> str:
        return f'about employee :{Person.__repr__(self)},{self.id},{self.rank},{Employee.employee_count}'
    
class Intern(Person):
    '''this class is Intern class. that shows everything about Interns '''
    intern_count=0
    time_intern='12 month'
    def __init__(self, fname, lname,) -> None:
        super().__init__(fname, lname)
        Intern.intern_count+=1

    def __hash__(self) -> int:
        return hash(Intern.intern_count,super().__hash__())

    def __repr__(self) -> str:
        return f'about intern: {Person.__repr__(self)},{Intern.time_intern},{Intern.intern_count}'

#instance of all class children
Mangager1=Mangager('simon','calive',5,23000)
Mangager2=Mangager('Nikol','mosaka',2,9000)
list_Manager=[Mangager1,Mangager2]
print((list_Manager))

Employee1=Employee('Sara','Viliom',987,'A')    
Employee2=Employee('Siri','nonee',687,'B') 
list_Employee=[Employee1,Employee2]
print(list_Employee)

Intern1=Intern('Neko','Dfrm')
list_Intern=[Intern1]
print(list_Intern)
