def exceptionAge(age):
    if isinstance (age,str):
        raise RuntimeError('please write number')
    elif (age>120 or age<1):
        raise RuntimeError('please write true age')
    elif isinstance(age,float):
        raise RuntimeError('don not write float')
    return age

try:
    number=exceptionAge(input('please write your age'))
    
except RuntimeError as error :
    print(error)
else:
    print('\t','number')