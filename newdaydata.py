import requests
from bs4 import BeautifulSoup


url = 'https://finance.yahoo.com/most-active'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', attrs={'class': 'W(100%)'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
print(["Symbol", "Name", "Price", "Change", "% Change", "Volume*", "Avg Volume(3m)", "Market Cap", "P/E Ratio (TTM)", "52 Week Range"])
print(*list_of_rows, sep='\n')


#outfile = open("./" + ticker + ".csv", "w")
#writer = csv.writer(outfile)
#writer.writerow(["Date", "Open", "High", "Low", "Close*", "Adj Close**", "Volume"])
#writer.writerows(list_of_rows)
