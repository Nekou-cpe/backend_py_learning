'''https://docs.python.org/3/library/operator.html ->operator methods
overloading operator method'''
class Math():
    def __init__(self,num) -> None:
        self.num=num

    def __eq__(self, object1) -> bool:
        return self.num == object1.num 
    
    def __sub__(self, object1):
        return self.num - object1.num

    def __pow__(self, object1):
        return self.num**object1.num  

number1=Math(13)
number2=Math(2)
print(number1-number2)
