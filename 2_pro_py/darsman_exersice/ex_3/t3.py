class Product_Price():
    def __init__(self,list_price) -> None:
        self.list_price=list_price
    
    def __add__(self,obj):
        self.sum=sum([product for product in self.list_price])
        self.count=len(self.list_price)
        obj.sum=sum([product for product in obj.list_price])
        obj.count=len(obj.list_price)
        self.avg=self.sum/self.count
        self.avg_off=self.avg*0.8
        obj.avg=obj.sum/obj.count
        obj.avg_off=obj.avg*0.8
        return f'store1 avg: {self.avg}, store2 avg: {obj.avg} , store1 avg off :{self.avg_off} ,store2 avg off :{obj.avg_off}'

    def __eq__(self, obj) -> bool:
        list_bool=[]#store 2 if less then its tru
        counter=0
        for product1 in self.list_price:
            for product2 in obj.list_price:
                if product1<product2:
                    list_bool.append(False)
                elif product1>product2:
                    list_bool.append(True)
        for i in list_bool:
            if i is True:
                counter+=1
            else:
                counter-=1
        if counter>0:
            return f'store 2 has better price'

        elif counter<0:
            return f'store 1 has better price'
        
        else :
            return f'store1 and store 2 have same price'

    def __str__(self) -> str:
        return f'{self.list_price}'

#instances
Product_Price_List1=[5000,10000,15000,6000,25000,12000,14000,10000,7000,20000]
Product_Price1=Product_Price(Product_Price_List1)
Product_Price_List2=[4000,12000,16000,5000,22000,10000,16000,11000,5000,18000]
Product_Price2=Product_Price(Product_Price_List2)
print(Product_Price1.__add__(Product_Price2))
print(Product_Price1.__eq__(Product_Price2))

