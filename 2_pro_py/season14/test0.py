import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",       
    user="root",           
    password="400130",
    database="newsdb"   
)
if conn.is_connected():
    print('connected')