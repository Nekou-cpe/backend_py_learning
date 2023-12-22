'''delivery price'''
from enum import Enum
from abc import ABC , abstractmethod

class Order:
    def __init__(self) -> None:
        pass

#--------------------------------
class Item(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_cost(self):
        pass

#--------------------------------
class Pizza:
    def __init__(self) -> None:
        pass
class Size(Pizza,Enum):
    On=200
    Two=500
    Big=1000
class Vegtable(Pizza):
    def __init__(self) -> None:
        pass

class Meat(Pizza):
    def __init__(self) -> None:
        pass

class Chisse(Pizza):
    def __init__(self) -> None:
        pass

#--------------------------------
class Dirink:
    def __init__(self) -> None:
        pass
#--------------------------------
class Delivery(Enum):
    Bike=20
    Motor=30
    Car=50