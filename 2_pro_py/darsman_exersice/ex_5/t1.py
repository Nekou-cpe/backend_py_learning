class ExceptionHandeling(Exception):
    def __init__(self, massage):
        super().__init__(massage)
        self.massage=massage
    
    def __repr__(self):
        return f' Error is :{self.massage}'
        
class ChosePlayer():
    def __init__(self,id,age,tall,weight):
        self.id=id
        self.age=age
        self.tall=tall
        self.weight=weight
    
    def tallValidation(self):
        if not self.check_int(self.tall):
            raise ExceptionHandeling('this tall is not integer')
        self.tall=int(self.tall)
        if not 170<self.tall<190:
            raise ExceptionHandeling('Error tall between 170 to 190 ')
        return f'tall: {self.tall}'
    
    def weigh_ageValidation(self):
        if not self.check_float(self.weight):
            raise ExceptionHandeling('weight is not float')
        if not self.check_int(self.age):
            raise ExceptionHandeling('age is not integer')
        self.age=int(self.age)
        self.weight=float(self.weight)
        if not 15<=self.age<=25:
            if not 60<self.weight<80:
                raise ExceptionHandeling('Error weight between 60 t0 80')
            raise ExceptionHandeling('age between 15 to 25')
        elif not 25<self.age<=35:
            if 50<self.weight<75:
                raise ExceptionHandeling('Error weight between 50 t0 75')
            raise ExceptionHandeling('age between 25 vto 35')
        return f'weight: {self.weight},age: {self.age}'

    
    def playerRegister(self):
        try:
            self.tallValidation()
            self.weigh_ageValidation()
            return f'this person with id: {self.id},{self.age},{self.weight},{self.tall} is accepted'
        except ExceptionHandeling as error:
            return f'Error is :{error}'
    
    @staticmethod
    def check_float(num):
        try:
            float(num)
            return True
        except ValueError as error:
            print(error)

    @staticmethod
    def check_int(num):
        try:
            int(num)
            return True
        except ValueError as error:
            print(error)
    
    def __repr__(self):
        pass
players=[]
while True:
    kepper=input('pleas write 0 for breake,enter for keep going')
    if not kepper=='0':
        id=input('enter id')
        age=input('enter age')
        weight=input('enter weight')
        tall=input('enter tall')
        player=ChosePlayer(id,age,tall,weight)
        players.append(player.playerRegister())

    else:
        break

for p in players:
    print(p)
