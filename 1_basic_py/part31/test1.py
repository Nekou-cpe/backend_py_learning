''' values can be : public __privet _protect'''

class pc():

    def __init__(self,name) -> None:
        self.__name=name

    def __str__(self) -> str:
        return f'name of your computer is : {self.__name}'

pc1=pc('Apple')
pc1.__name='Lenovo'
print(pc1)