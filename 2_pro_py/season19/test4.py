import numpy as np
from numpy import random

x=random.rand(3) #random between 0 to 1 inside an array
print(x)

y=random.randint(9,100,size=(20,20))
print(y)

z=random.choice([10,13,656,56,86,878],size=(2,2))
print(z)

