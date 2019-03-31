'''
@author: Hank Kahl
Created on Mar 31, 2019

UpdateWeather
'''
import json
import requests
import mysql.connector
import time

if __name__ == '__main__':
    pass
def getWeather(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    api_key = '1975e8da186959be52b7f1cd93e1bfdc'
    response = requests.get(base_url + 'APPID='+ api_key+'&q='+city)
    x = response.json()
    y = x['main']
    tMin = round((y['temp_min']- 273.15) * 9/5 + 32,1) 
    tMax = round((y['temp_max']- 273.15) * 9/5 + 32,1)
    #     print tMin,tMax
    return str(tMin)+'/'+str(tMax)

#===============================================================================
# # mountain = (name, weather,website, address)
#===============================================================================

mydb = mysql.connector.connect(
    host = '35.229.56.253',
    user = 'root',#'calm-segment-236201:us-east:skiieasydb',
    passwd = 'MLHProgrammersNow',
    database = 'ski_prices'
    )
mycursor = mydb.cursor()
while True:
    mycursor.execute('Update mount_ids set weather = %s where mount_name = %s',(getWeather('Macungie'),'Bear Creek'))
    mycursor.execute('Update mount_ids set weather = %s where mount_name = %s',(getWeather('White Haven'),'JFBB'))
    mycursor.execute('Update mount_ids set weather = %s where mount_name = %s',(getWeather('Tannersville'),'Camelback'))
    mydb.commit()
    time.sleep(216000)# 1 hour
# bear = ('Bear Creek', getWeather('Macungie'), 'https://www.bcmountainresort.com/', '101 Doe Mountain Ln, Macungie, PA 18062' )
# jf = ('JFBB',getWeather('White Haven'),'http://www.jfbb.com/','434 Jack Frost Mountain Rd, White Haven, PA 18661')
# camel = ('Camelback',getWeather('Tannersville'),'https://www.skicamelback.com/',' 301 Resort Dr, Tannersville, PA 18372')


