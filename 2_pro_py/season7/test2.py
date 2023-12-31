'''Decorators 1'''
def mainFunction(func):
    for j in range(4): print(func())
    
@mainFunction
def function1():
    return f'******'

function1