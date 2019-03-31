'''
@author: Hank Kahl
Created on Mar 30, 2019

jfbb
'''
from ScrapeFunctions import *
if __name__ == '__main__':
    pass
raw_html = getHTML('https://www.jfbb.com/snow-passes/')
html = BeautifulSoup(raw_html, 'html.parser')
Blue = []
TicketType = {1:'all day',7:'night',3:'all day',7:'night'}
Adult = [1,7]
Senior = [3,7]
Youth = [3,7]
DoW = ['MTWR','FSUH']
Tickets = []

r=0
for tr in html.select('tr'):
    c = 0
    for td in tr.select('td'):
        comment = ''
        if c != 0:
            if r == 7: comment = 'only at BB'
            price = []
            if r in Adult:
#                 print str(td.text)[-2:]
                price = (DoW[c-1], TicketType[r],'Adult', int(str(td.text)),comment)
                Tickets.append(price)
            if r in Senior:
#                 print str(td.text)[-2:]
                price = (DoW[c-1], TicketType[r],'Senior', int(str(td.text)), comment)
                Tickets.append(price)
            if r in Youth:
#                 print str(td.text)[-2:]
                price = (DoW[c-1], TicketType[r],'Youth', int(str(td.text)),comment)
                Tickets.append(price)
#         print r,c,'\t', td.text
        c+=1
    r+=1
# Tickets.append(['MTWRFSUH','all day','Military',25,''])
Tickets.append(('MTWRFSUH','all day','Tot',10,''))
# print len(Tickets)
# for ticket in Tickets:
#     print ticket
