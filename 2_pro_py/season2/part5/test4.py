from multipledispatch import dispatch

@dispatch(str,str)
def upperCase(str1,str2):
    str1=str1.upper()
    str2=str2.upper()
    return str1+' '+str2
@dispatch(str,str,str)
def upperCase(str1,str2,str3):
    str1=str1.upper()
    str2=str2.upper()
    str3=str3.upper()
    return str1+' '+str2+' '+str3


print(upperCase('hello','world'))
print(upperCase('hello','world','my love'))