import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydb" 
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE student (name VARCHAR(255), age INTEGER(20)")

sql = "INSERT INTO student (Name, Age) VALUES (%s,%s)"
val = ("Aravindh", 21)
mycursor.execute(sql, val)
mycursor.execute("DELETE from student WHERE Name='Aravindh'")
mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
