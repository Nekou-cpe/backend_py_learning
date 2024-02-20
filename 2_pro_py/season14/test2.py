from mysql.connector import connect,Error
'''creating new tables'''
try:
    with connect() as db:
        myCursor=db.cursor()
        user='''CREATE TABLE user(
            user_id INT NOT NULL UNIQUE AUTO_INCREMENT,
            user_pass INT NOT NULL,
            user_fname VARCHAR(20) NOT NULL,
            user_lname VARCHAR(30) NOT NULL,
            age INT,
            phon INT NOT NULL,
            email varchar(50)
            )'''
        myCursor.execute(user)
        db.commit()
        print('done updating...')
except Error as error:
    print(error)