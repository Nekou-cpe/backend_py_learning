import json
import os
#seriallizing obj
os.chdir('2_pro_py\\season11\\file2')
Student1={"name":"Nekou","age":20,"id":400130100}
Student2={"name":"Nikol","age":22,"id":400130183}
Students=[Student1,Student2]
if not(os.path.exists('test2.json')):
    with open('test3.json','w') as f1:
        f1.write(json.dumps(Students))
        json.dump(Students,f1,indent=2)
else:
    print('this work is already done!!!')
        
