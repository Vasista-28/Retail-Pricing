import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2812",
    database="testdatabase"
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdatabase")