"""3th form of overloading"""

def summ(datatype,*arg):
    
    if (datatype=='int'):
        s=0
    elif (datatype=='str'):
        s=str()
    for i in arg:
        s+=i
    return s

print(summ('int',10,13,14,13))
print(summ('str','hek','hello','ss'))
    