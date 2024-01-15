#diseriallization -> laods=use str insid python / load=use str from json file to python
import json
import os
import demjson3
print(os.getcwd())
#loads for deseriallization:
str_desriall='''[{"fname":"Nekou","lname":"Dfrm","Code":4467,"age":20},
                {"fname":"Nikol","lname":"Dfrm","Code":4451167,"age":20},
                {"fname":"Sara","lname":"hofman","Code":4467,"age":22}]'''
print(type(str_desriall))
str_list=json.loads(str_desriall)
print(str_list)
print(type(str_list))
#load for deseriallz
with open('2_pro_py\\season11\\file1\\test.json','r') as f1:
    list_json=json.load(f1)
print(list_json)




