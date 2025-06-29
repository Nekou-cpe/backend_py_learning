import inspect

def universal_decorator(func):
    def wrapper(*args, **kwargs):
        # Check if first argument is 'self' (for methods)
        is_method = inspect.ismethod(func) or (args and hasattr(args[0], '__class__'))

        print("Before execution" + (" (method)" if is_method else " (function)"))
        res = func(*args, **kwargs)
        print("After execution" + (" (method)" if is_method else " (function)"))
        return res
    return wrapper

class MyClass:
    @universal_decorator
    def say_hello(self):
        print("Hello!")

@universal_decorator
def testFunc():
    print("Test function running")
    return 30

# Run tests
obj = MyClass()
obj.say_hello()

func_t = testFunc()
print(func_t)
