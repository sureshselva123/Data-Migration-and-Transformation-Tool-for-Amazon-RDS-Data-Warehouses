#1-- further steps to get the data


# need to Run  the connection  object
# Connect to your Amazon RDS instance
connection = mysql.connector.connect(
    host="swathidb1.c3gy2i8oqu9v.us-west-2.rds.amazonaws.com",
    user="admin",
    password="Suresh123",
    database="mydatabase"
    
)
cursor = connection.cursor()
cursor.execute('use mydatabase')

#cursor.execute('create database mydatabase')
#cursor.execute('show databases')
#for x in cursor:
   # print (x)

#2--show database

cursor.execute('show databases')
for x in cursor:
    print (x)

#3--using select statement to get data

cursor.execute("SELECT * FROM url_data")
 
# Fetch and process the results
my_results = cursor.fetchall()
for row in my_results:
    print(row)