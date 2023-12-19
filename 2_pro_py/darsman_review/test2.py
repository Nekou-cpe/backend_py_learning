class Employee():
    def __init__(self,fname,lname,address,mobile) -> None:
        self.fname=fname
        self.lname=lname
        self.address=address
        self.mobile=mobile

    def bime_calcul(self,income):
        self.bime=income*0.1
        return self.bime
    
    def __str__(self) -> str:
        return f'{self.fname},{self.lname},{self.address},{self.mobile}'
    
class Employee_official(Employee):
    def __init__(self, fname, lname, mobile,address, income,childs,st,hoursWork,incomeHour,daysWork) -> None:
        super().__init__(fname, lname, mobile, address)
        self.childs=childs
        self.st=st  
        self.__income=income
        self.hoursWork=hoursWork
        self.incomeHour=incomeHour
        self.daysWork=daysWork
    
    def income_calculate(self):
        if self.daysWork>=30:
            self.__realIncome=self.__income+(self.hoursWork*self.incomeHour)-super().bime_calcul(self.__income)
            return self.__realIncome
        else:
            return 'there is not time to give your money'
  
    def __str__(self) -> str:
        return f'{super().__str__()},{self.childs},{self.st}'

class Employee_unofficial(Employee):
    def __init__(self, fname, lname, address,mobile, income,daysWork) -> None:
        super().__init__(fname, lname,address, mobile)
        self.__income=income
        self.daysWork=daysWork

    def income_calculate(self):
        self.__realIncome=(self.daysWork*self.__income)
        return self.__realIncome
    
    def __str__(self) -> str:
        return f'{super().__str__()}'
    
employee_official1=Employee_official('Nekou','Dfrm','1323445','something121','200000',None,'single',56,20,33)
print(employee_official1)
employee_unofficial1=Employee_unofficial('Nikol','Dfrm','somthingElse','97458983934',500,21)
print(employee_unofficial1)