from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,fname,lname,code,field,adrress):
        self.fname=fname
        self.lname=lname
        self.__code=code
        self.field=field
        self.adrress=adrress
    
    @abstractmethod
    def calculateScore(self):
        pass

    @property
    def codegetter(self):
        return self.__code

    @codeSetter.setter
    def codeSetter(self,code):
        self.__code='@'+code

    def accept(self):
        if 90<=self.full_score:
            return f'this student {self.__code} is accepted'
        else:
            return f'this student {self.__code} is not accepted'

    def __repr__(self):
        pass

class FreeParticipants(Person):
    def __init__(self,fname,lname,code,field,adrress,inter_score,wrt_score):
        Person.__init__(self,fname,lname,code,field,adrress)
        while not ((100>inter_score>0) and (100>wrt_score>0)):
            print('please enter scores between 0 to 100')
            inter_score=input('intwrview score: ')
            wrt_score=input('writeing score: ')
        self.inter_score=inter_score
        self.wrt_score=wrt_score

    def calculateScore(self):
        self.full_score=(self.wrt_score+self.inter_score)/2
        return self.full_score


class JiniosStd(Person):
    def __init__(self,fname,lname,code,field,adrress,gpa_score,uni_score):
        Person.__init__(self,fname,lname,code,field,adrress)
        self.list_gpa=[100,80,60]
        self.gpa_score=self.list_gpa[gpa_score-1]


        

    def calculateScore(self):
        self.full_score=(self.gpa_score+self.uni_score)/2
        return self.full_score


class EmployeeCompany(Person):
    def __init__(self,fname,lname,code,field,adrress,avg_score,history,):
        Person.__init__(self,fname,lname,code,field,adrress)
        self.avg_score=avg_score
        self.history=history

    def calculateScore(self):
        self.full_score=self.avg_score+(self.avg_score*self.history)
        return self.full_score
    



