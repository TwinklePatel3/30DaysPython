#                              💻 Exercises: Day 22
import json
import requests
from bs4 import BeautifulSoup

# 1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
data_list = []

for data in soup.find_all("div", class_="facts-wrapper"):
    data_dict = {}

    category = data.find('h5')
    data_dict["category"] = category.text
    row = data.find_all('ul', class_="row list")
    for l in row:
        list = l.find_all('li')
        for i in list:
            item = i.find('p').text
            count = i.find('span').text
            # print(item, count)
            data_dict[item] = count
    data_list.append(data_dict)

with open("./data/scarp_data.json", 'w') as f:
    f.write(json.dumps(data_list, indent=8))


# 2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

# ////////////////////// GIVEN URL IS NOT WORKING SO I PERFORMED THIS TASK WITH DIFFERENT URL ?//////////////

url = 'https://www.w3schools.com/html/html_tables.asp'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')
header = []
data = []
for i, row in enumerate(table.find_all('tr')):
    dict = {}
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        for i, el in enumerate(row.find_all('td')):
            row = el.text.strip()
            dict[header[i]] = row
        data.append(dict)
# print(data)
with open("./data/table_data.json", 'w') as f:
    f.write(json.dumps(data, indent=8))


# 3. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.table
header = []
data = []
dict_data = []
for i, row in enumerate(table.find_all('tr')):
    dict = {}
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        counter = 0

        for j, el in enumerate(row.find_all(['th', 'td', 'img'])):
            r = el["src"] if el.name == "img" else el.text.strip()
            if r == "":
                continue

            if counter < 7:
                dict[header[counter]] = r
                counter += 1
            else:
                counter = 0
        data.append(dict)
print(data)
with open("./data/president_data.json", 'w') as f:
    f.write(json.dumps(data, indent=8))
