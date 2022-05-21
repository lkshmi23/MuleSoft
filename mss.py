import sqlite3

connection = sqlite3.connect('moviesDB.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movie
              (MOV_NAME VARCHAR(20),ACTOR VARCHAR(20),ACTRESS VARCHAR(20),DIRECTOR VARCHAR(20),YEAR INT)''')
query = """INSERT INTO movie VALUES ('Jab we met','Shahid Kapoor','Kareena Kapoor','Imtiaz Ali',2014)"""
query1 = """INSERT INTO movie VALUES ('YJHD','Ranbir Kapoor','Deepika Padukone',' Ayan Mukerji',2013)"""
query2 = """INSERT INTO movie VALUES ('Shershah','Siddharth Malhotra','Kiara Advani','Vishnuvardhan',2021)"""
count = connection.execute(query)
count1 = connection.execute(query1)
count2 = connection.execute(query2)
connection.commit()
print('Established Connection')
connection.close()



connection = sqlite3.connect('moviesDB.db')
cur = connection.cursor()
s1 = """SELECT * FROM movie"""
cur.execute(s1)
cur.execute("SELECT * FROM movie WHERE YEAR= 2014")
result = cur.fetchall()
print(result)
connection.commit()
connection.close()




