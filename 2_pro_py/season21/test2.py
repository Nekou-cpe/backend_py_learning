'''learning how write testing for our project:
2-unitest framework
'''

def summ(n,m):
    return n+m

def sub(n,m):
    return n-m

def mul(n,m):
    return n*m

def div(n,m):
    if m==0:
        raise ZeroDivisionError
    return n/m