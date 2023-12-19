class Product:
    def __init__(self,name,brand,price) -> None:
        self.name=name
        self.brand=brand
        self.price=price

    def __str__(self) -> str:
        return f'name of product : {self.name} \t brand : {self.brand} \t price :{self.price} \t'
class Food(Product):
    def __init__(self, name, brand, price,expire) -> None:
        super().__init__(name, brand, price)
        self.expire=expire

    def __str__(self) -> str:
        return f'{super().__str__()}expire :{self.expire}'
class Clothe(Product):
    def __init__(self, name, brand, price,color,size,model,material) -> None:
        super().__init__(name, brand, price)
        self.color=color
        self.model=model
        self.size=size
        self.material=material

    def __str__(self) -> str:
        return f'{super().__str__()}color: {self.color} \tmodel: {self.model}\tsize: {self.size}\tmaterial: {self.material}'

class Digital(Product):
    def __init__(self, name, brand, price,color,model) -> None:
        super().__init__(name, brand, price)
        self.color=color
        self.model=model

    def __str__(self) -> str:
        return f'{super().__str__()}\tcolor: {self.color}\tmodel: {self.model}'
    
    def __del__(self):
        print(f'deleted {self.name} of {self.brand}...')

food1=Food('nodel','nodelll',89,'2024/3/4')
clothe1=Clothe('clothe','H&M',4000,'black','xlarge','T-shirt','cotton')
digital1=Digital('mobile','apple',9000,'black','pro15')
print(food1)
print(clothe1)
print(digital1)