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
    def Code(self):
        return self.__code

    @Code.setter
    def Code(self,code):
        self.__code='@'+code

    @abstractmethod
    def accept(self):
        pass

    def __repr__(self):
        return f'first name:{self.fname}, lname: {self.lname},field:{self.field},address:{self.adrress}'

class FreeParticipants(Person):
    def __init__(self,fname,lname,code,field,adrress,inter_score,wrt_score):
        Person.__init__(self,fname,lname,code,field,adrress)
        self.inter_score=inter_score
        self.wrt_score=wrt_score
        while True:
            if (0 <= self.inter_score <= 100) and (0 <= self.wrt_score <= 100):
                break

            else:
                print("❌ Please enter a valid number between 0 and 100.")
                self.inter_score=int(input('enter intern score'))
                self.wrt_score=int(input('enter wrt score'))

    def calculateScore(self):
        self.full_score=(self.wrt_score+self.inter_score)/2
        return self.full_score

    def accept(self):
        if 90<=self.full_score:
            return f'this student {self.Code} is accepted'
        else:
            return f'this student {self.Code} is not accepted'

    def __repr__(self):
        parent=Person.__repr__(self)
        return f'{parent},score: {self.calculateScore()},{self.accept()}'


class JiniosStd(Person):
    def __init__(self,fname,lname,code,field,adrress,gpa_score,uni_score):
        Person.__init__(self,fname,lname,code,field,adrress)
        self.list_gpa=[100,80,60]
        self.gpa_score=self.list_gpa[gpa_score-1]
        if 17.5>uni_score>=16:
            self.uni_score=60
        elif 18.5>uni_score>=17.5:
            self.uni_score=80
        elif uni_score>=18.5:
            self.uni_score=100
        else:
            print('please write true uni score')

    def calculateScore(self):
        self.full_score=(self.gpa_score+self.uni_score)/2
        return self.full_score

    def accept(self):
        if 90<=self.full_score:
            return f'this student {self.Code} is accepted'
        else:
            return f'this student {self.Code} is not accepted'

    def __repr__(self):
        parent=Person.__repr__(self)
        return f'{parent},score: {self.calculateScore()},{self.accept()}'

class EmployeeCompany(Person):
    def __init__(self,fname,lname,code,field,adrress,avg_score,history):
        Person.__init__(self,fname,lname,code,field,adrress)
        self.avg_score=avg_score
        if 5>=history>=1:
            self.history=0.1
        elif history>5:
            self.history=0.2

    def calculateScore(self):
        self.full_score=self.avg_score+(self.avg_score*self.history)
        return self.full_score

    def accept(self):
        if 0<=self.full_score<=120:
            return f'this student {self.Code} is accepted'
        else:
            return f'this student {self.Code} is not accepted'

    def __repr__(self):
        parent=Person.__repr__(self)
        return f'{parent},score: {self.calculateScore()},{self.accept()}'
    
###################instance
participants_List = []
for i in range(1):
    name = input("Enter Name: ")
    family = input("Enter Family: ")
    id_Number = input("Enter Id Number: ")
    major = input("Enter Major: ")
    address = input("Enter Address: ")
    score1 = int(input("Enter Test Score1: "))
    score2 = int(input("Enter Test Score2: "))
    pf = FreeParticipants(name,family,id_Number,major,address,score1,score2)
    participants_List.append(pf)

for i in range(1):
    name = input("Enter Name: ")
    family = input("Enter Family: ")
    id_Number = input("Enter Id Number: ")
    major = input("Enter Major: ")
    address = input("Enter Address: ")
    score1 = int(input("Enter Test Score1: "))
    score2 = float(input("Enter Test Score2: "))
    pf = JiniosStd(name,family,id_Number,major,address,score1,score2)
    participants_List.append(pf)

for i in range(1):
    name = input("Enter Name: ")
    family = input("Enter Family: ")
    id_Number = input("Enter Id Number: ")
    major = input("Enter Major: ")
    address = input("Enter Address: ")
    score1 = int(input("Enter Test Score1: "))
    score2 = int(input("Enter Test Score2: "))
    pf = EmployeeCompany(name,family,id_Number,major,address,score1,score2)
    participants_List.append(pf)

for i in participants_List:
    print(i)