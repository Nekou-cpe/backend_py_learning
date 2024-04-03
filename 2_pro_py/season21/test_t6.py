import t3
import pytest
#for big data other data
@pytest.mark.parametrize('num1,num2,res',
    [(1,2,3),(4,56,60),(0,87,87)]
)
def test_summ(num1,num2,res):
    assert num1+num2==res  

