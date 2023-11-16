'''Exception handeling 2'''
class ExceptionHandeling(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message=message

    def __str__(self) -> str:
        return f'this is Error :{self.message}'
    
def handeling_error(nm):
    if not isinstance(nm,str):
        raise ExceptionHandeling('write string value')
    if len(nm)<1 or len(nm)>20:
        raise ExceptionHandeling('write your name between 1 to 20')
    return nm

try:
    #name=input('write your name')
    new_name=handeling_error(1)
    print(new_name)
except ExceptionHandeling as error:
    print(error)