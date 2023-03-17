import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='*postgre0011#', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS File_Detail")

#Creating table as per requirement
sql ='''CREATE TABLE File_Detail(
   File_Name VARCHAR(40) NOT NULL,
   File_Path VARCHAR,
   Img_embedding VARCHAR
)'''
cursor.execute(sql)
print("Table created successfully........")
# conn.commit()
# #Closing the connection
# conn.close()