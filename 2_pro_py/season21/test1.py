'''learning how write testing for our project:
1-using doctest
ways:
python -m doctest -v test1.py
or import doctest'''

def cal(n,m):
    '''
    >>> cal(10,2)
    100
    >>> cal(10,0)
    1
    >>> cal(10,-1)
    0.1
    >>> cal(0,10)
    0
    '''
    r=n**m
    return r
import doctest
doctest.testmod()