import t3
import pytest

def test_summ():
    assert t3.summ(10,10)==20
    assert t3.summ(0,0)==0
    assert t3.summ(-10,10)==0
    assert t3.summ(10.1,10)==20.1      
    
def test_sub():
    assert t3.sub(10,10)==0
    assert t3.sub(-10,10)==-20
    assert t3.sub(0,0)==0
    assert t3.sub(-10,-10)==0

def test_mul():
    assert t3.mul(10,10)==100
    assert t3.mul(-10,10.1)==-101
    assert t3.mul(0,0)==0
    assert t3.mul(-10,10)==-100
    
def test_div():
    assert t3.div(10,10)==1
    assert t3.div(-10,10)==-1
    assert t3.div(0.1,10)==0.01
    assert t3.div(-10,0)==ZeroDivisionError

