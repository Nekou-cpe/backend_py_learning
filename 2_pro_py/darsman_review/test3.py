'''delivery price
bp=base price'''
from enum import Enum
from abc import ABC , abstractmethod
#--------------------------------Order
class Order:
    def __init__(self,Delivery) -> None:
        self.Delivery=Delivery
        self.order_item_list=[]

    def addItem(self,Item):
        self.order_item_list.append(Item)
        return sum(self.order_item_list)

#--------------------------------Item
class Item(ABC,Order):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def getCost(self):
        pass

#--------------------------------Pizza
class Pizza(Item):
    def __init__(self,Size) -> None:
        self.Size=Size
        self.Content_list=[]
        self.bp_pizza=4

    def addContent(self,newContent):
        self.Content_list.append(newContent) #search more

    def getCost(self):
        summ=0
        for self.newContent in self.Content_list: 
            summ+=Content.getPrice()
        summ=summ*self.Size+self.bp_pizza
        return summ

#--------------------------------Size
class Pizza_Size(Enum):
    On=200
    Two=500
    Big=1000

#--------------------------------Content
class Content(Pizza,ABC):
    @abstractmethod
    def getPrice(self):
        pass

#--------------------------------Eggplant
class Eggplant(Content):
    def __init__(self,weight_eggplant) -> None:
        super().__init__(self)
        if weight_eggplant>10:
            self.weight_eggplant=10
        else:
            self.weight_eggplant=weight_eggplant
        self.bp_Eggplant=0.7

    def getPrice(self):
        return self.weight_eggplant*self.bp_Eggplant
    
#--------------------------------Tomate
class Tomato(Content):
    def __init__(self,weight_tomato,canned) -> None:
        super().__init__(self)
        if weight_tomato>5:
            self.weight_tomato=5
        else:  
            self.weight_tomato=weight_tomato
        self.bp_tomato=0.9
        self.canned=canned
    
    def getPrice(self):
        if self.canned=='yes':
            return self.weight_tomato*self.bp_tomato*2
        else:
            return self.weight_tomato*self.bp_tomato

#--------------------------------Onion
class Onion(Content):
    def __init__(self,weight_onion) -> None:
        super().__init__(self)
        if weight_onion>3:
            self.weight_onion=3
        else:
            self.weight_onion=weight_onion
        self.bp_onion=0.3

    def getPrice(self):
        return self.weight_onion*self.bp_onion

#--------------------------------Lamb
class Lamb(Content):
    def __init__(self,weight_lamb) -> None:
        super().__init__(self)
        if weight_lamb>20:
            self.weight_lamb=20
        else:
            self.weight_lamb=weight_lamb
        self.bp_lamb=2

    def getPrice(self):
        return self.weight_lamb*self.bp_lamb
    
#--------------------------------Pork
class Pork(Content):
    def __init__(self,weight_pork) -> None:
        super().__init__(self)
        if weight_pork>30:
            self.weight_pork=30
        else:
            self.weight_pork=weight_pork
        self.bp_pork=1.5
    
    def getPrice(self):
        return self.weight_pork*self.bp_pork
    
#--------------------------------Bologna
class Bologna(Content):
    def __init__(self,weight_bologna) -> None:
        super().__init__(self)
        if weight_bologna>40:
            self.weight_bologna=40
        else:
            self.weight_bologna=weight_bologna
        self.bp_blogna=3
    
    def getPrice(self):
        return self.weight_bologna*self.bp_blogna

#--------------------------------Parmesan
class Parmesan(Content):
    def __init__(self,weight_parmesan) -> None:
        super().__init__(self)
        if weight_parmesan>10:
            self.weight_parmesan=10
        else:
            self.weight_parmesan=weight_parmesan
        self.bp_parmesan=0.9

    def getPrice(self):
        return self.weight_parmesan*self.bp_parmesan

#--------------------------------Chedar
class Chedar(Content):
    def __init__(self,weight_chedar) -> None:
        super().__init__(self)
        if weight_chedar>9:
            self.weight_chedar=9
        else:
            self.weight_chedar=weight_chedar
        self.bp_chedar=0.7

    def getPrice(self):
        return self.weight_chedar*self.bp_chedar

#--------------------------------Dirink
class Dirink(Enum):
    Water=10
    Cocka=15
    Beer=20
 
#--------------------------------Delivery
class Delivery(Enum):
    Bike=20
    Motor=30
    Car=50

#-------------------------------- instances
order_1=Order(Delivery.Bike.value)
Pizza_1=Pizza(Pizza_Size.Two.value)
Pizza_1.addContent(Tomato(0.2,'yes'))
Pizza_1.addContent(Lamb(0.8))
Pizza_1.addContent(Onion(0.1))
Pizza_1.addContent(Chedar(0.3))
print(Pizza_1.getCost())
'''Pizza_1.addContent(Tomato(0.2,'yes'))
Pizza_1.addContent(Chedar(0.2))
Pizza_1.addContent(Lamb(0.2))
Pizza_1.addContent(Onion(0.2))
print(Pizza_1.getCost())'''
