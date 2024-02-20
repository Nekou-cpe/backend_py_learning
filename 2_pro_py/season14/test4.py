from mysql.connector import connect,Error
'''select records'''
try:
    with connect() as db:
        myCursor=db.cursor()
        select='''SELECT * FROM user'''
        myCursor.execute(select)
        data_users=myCursor.fetchall()
        print(data_users)
        for data_user in data_users:
            print(data_user)
        db.commit()
        print('done updating...')
except Error as error:
    print(error)