from mysql.connector import connect,Error
'''creating new tables'''
try:
    with connect(host='localhost',user='root',password='400130',database='newsdb') as db:
        myCursor=db.cursor()

        comments='''
            create table comments(
                comment_id int not null unique ,
                count_likes int ,
                comment varchar(2000) not null,
                user_id int,
                FOREIGN key (user_id) REFERENCES user(user_id)
            );
            '''
        myCursor.execute(comments)
        db.commit()
        print('done updating...')
except Error as error:
    print(error)