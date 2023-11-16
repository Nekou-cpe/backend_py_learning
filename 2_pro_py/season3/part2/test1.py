'''Exception handeling 2
raise is same as return but works on Except'''
def handeling_error(nm):
    if not isinstance(nm,str):
        raise RuntimeError('write string value')
    if len(nm)<1 or len(nm)>20:
        raise RuntimeError('write your name between 1 to 20')
    return nm

try:
    #name=input('write your name')
    new_name=handeling_error(1)
    print(new_name)
except RuntimeError as error:
    print(error)
