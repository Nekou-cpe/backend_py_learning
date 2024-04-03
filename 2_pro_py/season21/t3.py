'''learning how write testing for our project:
3-pytest framework
'''

def summ(n,m):
    return n+m

def sub(n,m):
    return n-m

def mul(n,m):
    return n*m

def div(n,m):
    try:
        return n / m
    except ZeroDivisionError:
        return ZeroDivisionError
