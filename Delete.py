import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql@123",
    database = "podar"
)

cursor = db.cursor()
## defining the Query
query = "DELETE FROM students WHERE Rollno = 2"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()
print("roll no deleted")
