'''Enum'''
from enum import Enum

class Season(Enum):
	SPRING = 1
	SUMMER = 2
	AUTUMN = 3
	WINTER = 4

# printing enum member as string
print(Season.SPRING)

# printing name of enum member using "name" keyword
print(Season.SPRING.name)

# printing value of enum member using "value" keyword
print(Season.SPRING.value)

# printing the type of enum member using type()
print(type(Season.SPRING))

# printing enum member as repr
print(repr(Season.SPRING))

# printing all enum member using "list" keyword
print(list(Season))

