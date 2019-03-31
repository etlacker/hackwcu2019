'''
@author: Hank Kahl
Created on Mar 31, 2019

UpdateMountains
'''
import BearCreek, jfbb, CamelBack
import mysql.connector
import time

if __name__ == '__main__':
    pass
def updateTickets(mycursor,mountain,tickets):
    for line in tickets:
        sql = "Update prices set price = %s where mount_id = (select mount_id from mount_ids where mount_name = %s)and day_type = %s and ticket_type = %s and person_type = %s"
        val = tuple(line[-2], mountain) + line[:-2]
    #         val[-2] = str(val[-2])
        mycursor.execute(sql,val)


mydb = mysql.connector.connect(
    host = '35.229.56.253',
    user = 'root',#'calm-segment-236201:us-east:skiieasydb',
    passwd = 'MLHProgrammersNow',
    database = 'ski_prices'
    )
mycursor = mydb.cursor()
while True:
    updateTickets(mycursor, 'Bear Creek', BearCreek.Tickets)
    updateTickets(mycursor, 'JFBB', jfbb.Tickets)
    updateTickets(mycursor, 'Camelback', CamelBack.Tickets)
    mydb.commit()
    time.sleep(604800) # 1 week
