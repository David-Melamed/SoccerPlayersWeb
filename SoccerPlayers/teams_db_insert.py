from datetime import datetime

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="soccer_players",
    ssl_disabled=True
)
mycursor = mydb.cursor()
sqlFormula = "INSERT INTO my_app_teams (city, country, start_date, coach_name) VALUES (%s, %s, %s, %s) "
item = ("Paris", "France", 30/7/1992, "Mauricio Pochettino")
mycursor.execute(sqlFormula, item)
mydb.commit()


# mycursor.execute("CREATE TABLE items (product_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, product_type VARCHAR(255), "
#                  "gender VARCHAR(50) , "
#                  "age INTEGER(10), color VARCHAR(255))")
