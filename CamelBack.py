'''
@author: Hank Kahl
Created on Mar 30, 2019

CamelBack
'''
from ScrapeFunctions import *
if __name__ == '__main__':
    pass
raw_html = getHTML('https://www.skicamelback.com/tickets-passes/poconos-skiing/')
html = BeautifulSoup(raw_html, 'html.parser')
Blue = []
TicketType = ['all day', 'night']
Adult = [1,7,13, 19]
Senior = [2,8,14,20]
Youth = [2,8,14, 20]
Military = [5,11,17]
Tickets = []

r=0
for tr in html.select('tr'):
    c = 0
    for td in tr.select('td'):
        comment = ''
        if r < 7:
            DoW = 'MTWR'
        elif r<13:
            DoW = 'F'
        elif r < 19:
            DoW = 'SH'
        else: DoW = 'U'
        if c != 0:
            if r == 7: comment = 'only at BB'
            price = []
            if r in Adult:
#                 print str(td.text)[-2:]
                price = (DoW, TicketType[c-1],'Adult', int(str(td.text).strip()[-2:]),'')
                Tickets.append(price)
            if r in Senior:
#                 print str(td.text)[-2:]
                price = (DoW, TicketType[c-1],'Senior', int(str(td.text).strip()[-2:]), 'Seniors 70+ ski FREE')
                Tickets.append(price)
            if r in Youth:
#                 print str(td.text)[-2:]
                price = (DoW, TicketType[c-1],'Youth', int(str(td.text).strip()[-2:]),'')
                Tickets.append(price)
            if r in Military and c!=2:
                price = (DoW, TicketType[c-1],'Military', int(str(td.text).strip()[-2:]),'')
                Tickets.append(price)

#         print r,c,'\t', td.text
        c+=1
    r+=1
# Tickets.append(['MTWRFSUH','all day','Military',25,''])
Tickets.append(('MTWRFSUH','all day','Tot',0,''))
# print len(Tickets)
# for ticket in Tickets:
#     print ticket
