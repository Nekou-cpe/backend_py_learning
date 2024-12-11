import os
os.chdir('d:/backend_dev/darsman_py/2_pro_py/season10/file1/')

file1=open('test1.txt')
try:
    print(file1.readlines())
except Exception as error:
    print('error',error)
    
finally:
    file1.close()

print('done .. ')