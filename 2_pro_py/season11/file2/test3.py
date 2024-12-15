import json
import os
os.chdir('D:/backend_dev/darsman_py/2_pro_py/season11/file2')
#deserialized
#one obj
jsonStr1='{\"name\":\"Niko\",\"age\":21,\"code\":1234}'
obj1=json.loads(jsonStr1)
print(obj1)
print(type(obj1))

#more than one obj
jsonStr2='[{\"name\":\"Niko\",\"age\":21,\"code\":1234},{\"name\":\"Nikolas\",\"age\":22,\"code\":12}]'
obj_list1=json.loads(jsonStr2)
for obj in obj_list1:
    print(obj)
print(type(obj_list1))
print('------------------------')
#in another file
with open('test2.json','r') as f1:
    obj_list2=json.load(f1)
    for obj in obj_list2:
        print(obj)
