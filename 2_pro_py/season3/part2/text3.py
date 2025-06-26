def exceptionAge(age):
    try:
        inputt=int(age)
        
    except ValueError:
        try:
            float(age)
            raise RuntimeError('don not write float')
        except ValueError:
            raise RuntimeError('please write number')
                  
    else:
        if (inputt>120 or inputt<1):
            raise RuntimeError('please write true age') 
        return age

try:
    number=exceptionAge((input('please write your age')))
    
except RuntimeError as error :
    print(error)
else:
    print('\t',number)