from mysql.connector import connect,Error
'''create new database'''
try:
    with connect(host='localhost',user='root',password='400130',database='newsdb') as db:
        myCursor=db.cursor() #cursor can access to all db data
        myCursor.execute('SHOW DATABASES')
        for database in myCursor:
            print(database)
        myCursor.execute('CREATE DATABASE dbtest')
        print('database created...')
        myCursor.execute('drop database if exists dbtest')
        print('database deleted...')
        myCursor.execute('show databases')
        for database in myCursor:
            print(database)
except Error as error:
    print(error)