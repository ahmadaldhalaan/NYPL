import ssl
import mysql.connector
import db_params
import csv

# Create the DB connector
mydb = mysql.connector.connect(
        host=db_params.host,
        user=db_params.user,
        passwd=db_params.passwd,
        database=db_params.database)

mycursor = mydb.cursor()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

header = True
data = list()

with open('2020_06_16_07_01_04_data/MenuPage1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if header:
            header=False
        else:
            # Set empty int fields to NULL
            if row[1] ==  "":
                row[1] = None
            if row[2] ==  "":
                row[2] = None
            if row[4] ==  "":
                row[4] = None
            if row[5] ==  "":
                row[5] = None
            data.append(tuple(row))

num_records = len(data)
print(num_records, "records to insert.")

sql = "INSERT INTO MenuPage (id, menu_id, page_number, image_id, full_height, full_width, uuid) VALUES (%s, %s, %s, %s, %s, %s,%s)"

pos = 0
total_inserted = 0

# Insert posting records by blocks of 10000 into the database (bigger blocks caused memory issues)
while(pos < num_records):
    val = data[pos:pos+10000]
    mycursor.executemany(sql, val)
    total_inserted = total_inserted + mycursor.rowcount
    print(total_inserted, "records inserted.")
    pos = pos + 10000
    mydb.commit()
