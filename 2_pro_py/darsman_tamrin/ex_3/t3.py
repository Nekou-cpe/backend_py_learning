class Product_Price():
    def __init__(self,listt) -> None:
        self.list_price=listt
    
    def __it__(self,obj):
        self.sum=sum([product for product in self.list_price])
        obj.sum=sum([product for product in obj.list_price])
        return self.sum<obj.sum

    def __add__(self):
        pass


    def __mul__(self):
        pass

    def __str__(self) -> str:
        return f'{self.list_price}'

#instances
Product_Price_List1=[5000,10000,15000,6000,25000,12000,14000,10000,7000,20000]
Product_Price1=Product_Price(Product_Price_List1)
Product_Price_List2=[4000,12000,16000,5000,22000,10000,16000,11000,5000,18000]
Product_Price2=Product_Price(Product_Price_List2)
print('',Product_Price1.__it__(Product_Price2))

