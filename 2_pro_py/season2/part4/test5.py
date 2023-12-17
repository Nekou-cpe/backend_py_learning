'''inheritance
5)hybrid:'''
# This class is the base class
class Father:
    def func1(self):
        print("This function is in Father")

# This class inherits from Father
class FirstChild(Father):
    def func2(self):
        print("This function is in FirstChild")

# This class inherits from Father
class SecondChild(Father):
    def func3(self):
        print("This function is in SecondChild")

# This class inherits from both FirstChild and Father
class GrandChild(FirstChild, Father):
    def func4(self):
        print("This function is in GrandChild")

object = GrandChild()
object.func1() # This function is in Father
object.func2() # This function is in FirstChild
