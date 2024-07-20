import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql@123",
    database = "podar"
)

cursor = db.cursor()
print("Contents of the table: ")
cursor.execute("SELECT * from students")
print(cursor.fetchall())
