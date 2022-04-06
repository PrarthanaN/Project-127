from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

star = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(star)
soup = bs(page.text, 'html.parser')
star_table = soup.find('table')

tempList = []

table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)

starList = []

starName = []
starDistance = []
starMass = []
starRadius = []

for i in range(1, len(tempList)):
    starName.append(tempList[i][1])
    starDistance.append(tempList[i][3])
    starMass.append(tempList[i][5])
    starRadius.append(tempList[i][6])

data = pd.DataFrame(list(zip(starName, starDistance, starMass, starRadius)), columns = ['starName', 'starDistance', 'starMass', 'starRadius'])

data.to_csv('brightStars.csv')