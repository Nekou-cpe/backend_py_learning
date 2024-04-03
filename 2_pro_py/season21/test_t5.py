import t3
import pytest
#for big data or other data
@pytest.fixture
def data():
    list_data=[1,2,3,4,56,78,789,87,0]
    return list_data

def test_summ(data):
    assert t3.summ(1,0)==data[0]
    assert t3.summ(0,0)==data[8]
    assert t3.summ(77,10)==data[7]
    assert t3.summ(1,2)==data[2]     

