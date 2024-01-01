'''Introduction of using module :
1)you should import module
2) there are a few same function exist in all module:
    help(module_name)
    dir(module_name)
    module_name.__doc__ 
    module_name.__name__
    module_name.__cached__
    module_name.__file__   '''
import string
#help(string)
#print(dir(string))
#print(string.__file__)
#print(string.__name__)
#print(string.__cached__)

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)#shows digits exist in digit
print(string.printable)#shows all print able things
print(string.punctuation)#shows labels
temp_str=string.Template('my name is $name')
str_temped=temp_str.substitute(name='Nekou')
print(str_temped)
str1='neKOu dFrm'
print(string.capwords(str1))