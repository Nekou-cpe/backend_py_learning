import os

print(os.getcwd())
os.chdir('D:/backend_dev/darsman_py/2_pro_py/season10/file3')
if not os.path.exists('test1.py'):
    os.mkdir('test1.py')

for item in os.listdir():
    print(f'{item} : {os.path.isfile(item)}')   

