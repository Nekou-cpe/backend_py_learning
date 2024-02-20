from mysql.connector import connect,Error
'''add new records'''
try:
    with connect() as db:
        myCursor=db.cursor()
        values_list=[(1,234,'Nekou','Dfrm',20,99975937,'nekou@gmail.com'),
                     (2,433,'Nikolj','Dfrm',22,24524525,'nekouli@gmail.com')]
        
        myCursor.executemany("INSERT INTO user(user_id,user_pass,user_fname,user_lname,age,phon,email) VALUES (%s,%s,%s,%s,%s,%s,%s)",values_list)
        db.commit()
        print('done updating...')
except Error as error:
    print(error)