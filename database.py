
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2812",
    database="db1"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE db1")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE prices(inventory INTEGER(15) , cost INTEGER(15) , OPEX INTEGER(15), sellthrough INTEGER(15), profitpercentage INTEGER(15), perishability INTEGER(15))")

# mycursor.execute("SHOW TABLES")

# for tb in mycursor:
#     print(tb)

# mycursor.execute("DESCRIBE prices")
# for i in mycursor:
#     print(i)

# mycursor.execute("INSERT INTO prices(inventory,cost,OPEX,sellthrough,profitpercentage,perishability) VALUES (%s,%s,%s,%s,%s,%s)", (100,20,7,5,10,2))
# mydb.commit()

# mycursor.execute("select * from prices")
# for i in mycursor:
#     print(i)



# --------------------------------------------------------------------------------

mycursor.execute("SELECT JSON_ARRAYAGG(JSON_OBJECT('inventory', inventory, 'OPEX', OPEX, 'sellthrough', sellthrough, 'cost', cost, 'profitpercentage', profitpercentage , 'perishability', perishability)) from prices;")
print(mycursor)



# cursor = mydb.cursor()
# sql = "SELECT * FROM prices"
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for i in results:
#         inventory = i[0]
#         cost = i[1]
#         OPEX = i[2]
#         sellthrough = i[3]
#         profitpercentage = i[4]
#         perishability = i[5]
#         print(inventory, cost, OPEX, sellthrough,profitpercentage,perishability)

# except:
#     print("MG")

# mydb.close()



# ---------------------------------------------------------------------------------------------------





# def read_date_num_csv_to_sql(filep,user,passw,host,port,dbname): 
#     csv_data = pd.read_csv(filep, sep=",") 
#     df = pd.DataFrame(csv_data) 
#     df["dates"] = pd.to_datetime(df["dates"]) 
#     df["numbers"] = pd.to_numeric(df["numbers"]) 
 
#     engine = create_engine('mysql+pymysql://'+user+':'+passw+'@'+host+':'+port+'/'+dbname+'') 
#     # set index attribute to true to create index as a column, great for primary key column 
#     df.to_sql(name="dates_num", con=engine, if_exists="append", index=False) 
 
# read_date_num_csv_to_sql("/data.csv","root","somepassword","localhost","3306","db")







# mydb.commit()


# mycursor.execute("DROP DATABASE testdata")

# mycursor.execute("SELECT * FROM prices ")
# for i in mycursor:
#     print(i)
