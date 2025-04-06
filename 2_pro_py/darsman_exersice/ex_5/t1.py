class ChosePlayer():
    def __init__(self,id,age,tall,weight):
        self.id=id
        self.age=age
        self.tall=tall
        self.weight=weight
    def exceptionHandeling(self):
        if 170<self.tall<190:
            if 15<=self.age<=25:
                if 60<self.weight<80:
                        pass
                elif 25<self.age<=35:
                    if 50<self.weight<75:
                        pass
        