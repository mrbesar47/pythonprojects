import csv
import requests
from bs4 import BeautifulSoup

print('Do you want to see the list of the most active tickers today: [Y-yes, N-no] ')
val1 = input()
if val1 == 'Y' or val1 == 'y':
    import os
    os.system('python newdaydata.py')

# import pandas as pd

watchlist = []

while True:
    print('[enter 0 to exit] Enter the next ticker you want to track: ')
    val = input()
    if val == '-1':
        break
    watchlist.append(val)

page = 'https://finance.yahoo.com/quote/'
period = '/history?period1=1550448000&period2=1581984000&interval=1d&filter=history&frequency=1d'

for x in watchlist:
    ticker = x
    url = page + ticker + period
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', attrs={'class': 'W(100%) M(0)'})

    list_of_rows = []
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

    outfile = open("./" + ticker + ".csv", "w")
    writer = csv.writer(outfile)
    writer.writerow(["Date", "Open", "High", "Low", "Close*", "Adj Close**", "Volume"])
    writer.writerows(list_of_rows)
