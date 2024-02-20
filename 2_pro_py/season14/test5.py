from mysql.connector import connect,Error
'''deleting records'''
try:
    with connect() as db:
        myCursor=db.cursor()
        delete='''DELETE FROM user WHERE user_id=1'''
        myCursor.execute(delete)
        db.commit()
        print('done deleting...')
except Error as error:
    print(error)