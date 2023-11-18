
class XYZ():
    '''this class shows information about a company'''
    def __init__(self,name,maneger_name,address,count_employee,revenue) -> None:
        self.name=name
        self.maneger_name=maneger_name
        self.address=address
        self.count_employee=count_employee
        self.revenue=revenue
    
    def productivity(self): #shows productivity of company
        productive_employee= self.revenue/self.count_employee
        return productive_employee
    
    def __str__(self) -> str:
        return f'name of company {self.name} \n manager name {self.maneger_name} \n address {self.address} \n employee {self.count_employee} \n income {self.revenue}'
    

XYZ1=XYZ('Torob','Nikol','somewhere',390,87000000)
print(XYZ1.productivity())
print(XYZ1)




