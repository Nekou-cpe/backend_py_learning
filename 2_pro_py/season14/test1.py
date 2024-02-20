from mysql.connector import connect,Error
'''create new database'''
try:
    with connect() as db:
        myCursor=db.cursor()
        myCursor.execute('SHOW DATABASES')
        for database in myCursor:
            print(database)
        myCursor.execute('CREATE DATABASE dbtest')
        print('database created...')
except Error as error:
    print(error)