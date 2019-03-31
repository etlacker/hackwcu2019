'''
@author: Hank Kahl
Created on Mar 31, 2019

CamelBack
'''
import BearCreek, jfbb, CamelBack
import mysql.connector
from UpdateWeather import getWeather

def addTickets(mycursor,mountain,tickets):
    sql = "INSERT INTO mount_ids (mount_name, weather, website, address) VALUES (%s, %s, %s, %s)"
#         val = 'Bear Creek
    mycursor.execute(sql, mountain)
    for line in tickets:
#     line[-2] = float(line[-2])
    
        sql = "insert into prices(mount_id, day_type, ticket_type, person_type, price, comments) values((select max(mount_id) from mount_ids), %s, %s, %s, %s, %s)" 
        val = line
#         val[-2] = str(val[-2])
        mycursor.execute(sql,val)
        
#         sql = "INSERT INTO prices (ticket_id, weather, price, comments) VALUES ((select max(ticket_id) from ticket_ids),%s, %s, %s)"
#         val = tuple([''])+line[-2:]
#         print val
#         mycursor.execute(sql,val)
mydb = mysql.connector.connect(
    host = '35.229.56.253',
    user = 'root',#'calm-segment-236201:us-east:skiieasydb',
    passwd = 'MLHProgrammersNow',
    database = 'ski_prices'
    )
mycursor = mydb.cursor()
mycursor.execute('''
create table prices(
ticket_id int NOT NULL AUTO_INCREMENT,
mount_id int NOT NULL,
day_type varchar(8) NOT NULL,
ticket_type varchar(15) NOT NULL,
person_type varchar(15) NOT NULL,
price varchar(4) NOT NULL,
comments text NOT NULL,
PRIMARY KEY(ticket_id)
)
''')
mycursor.execute('''
create table mount_ids(
mount_id int NOT NULL AUTO_INCREMENT,
mount_name varchar(20) NOT NULL,
weather varchar(15) NOT NULL,
website varchar(200) NOT NULL,
address varchar(50) NOT NULL,
PRIMARY KEY(mount_id)
)''')

bear = ('Bear Creek', getWeather('Macungie'), 'https://www.bcmountainresort.com/', '101 Doe Mountain Ln, Macungie, PA 18062' )
jf = ('JFBB',getWeather('White Haven'),'http://www.jfbb.com/','434 Jack Frost Mountain Rd, White Haven, PA 18661')
camel = ('Camelback',getWeather('Tannersville'),'https://www.skicamelback.com/',' 301 Resort Dr, Tannersville, PA 18372')

addTickets(mycursor, bear, BearCreek.Tickets)
addTickets(mycursor, jf, jfbb.Tickets)
addTickets(mycursor, camel, CamelBack.Tickets)


# (Day_Type, Ticket_Type, Person_Type, Price, Comment)




# mycursor.execute("SHOW DATABASES")
# 
# for x in mycursor:
#   print(x)

mydb.commit()
