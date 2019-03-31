'''
@author: Hank Kahl
Created on Mar 30, 2019

BearCreek
'''
from ScrapeFunctions import *
if __name__ == '__main__':
    pass

raw_html = getHTML('https://www.bcmountainresort.com/play/snowsports/lift-tickets/')
html = BeautifulSoup(raw_html, 'html.parser')
TicketType = {1:"4 hour",2:'all day',3:'night',4:'4 hour',5:'all day',6:'night'}
Adult = [1,2,3]
Senior = [4,5,6]
Youth = [4,5,6]
DoW = ['MTWR','FSUH']
Tickets = []

r=0
for tr in html.select('tr'):
    c = 0
    for td in tr.select('td'):
        if c != 0 and r<7:
            price = ()
            if r in Adult:
#                 print str(td.text)[-2:]
                price = (DoW[c-1], TicketType[r],'Adult', int(str(td.text).strip()[-2:]),'')
                Tickets.append(price)
            if r in Senior:
#                 print str(td.text)[-2:]
                price = (DoW[c-1], TicketType[r],'Senior', int(str(td.text).strip()[-2:]), 'Seniors 70+ ski FREE')
                Tickets.append(price)
            if r in Youth:
#                 print str(td.text)[-2:]
                price = (DoW[c-1], TicketType[r],'Youth', int(str(td.text).strip()[-2:]),'')
                Tickets.append(price)
#         print r,c,'\t', td.text
        c+=1
    r+=1
Tickets.append(('MTWRFSUH','all day','Military',25,''))
Tickets.append(('MTWRFSUH','all day','Tot',0,''))
# print len(Tickets)               
# for ticket in Tickets:
#     print ticket