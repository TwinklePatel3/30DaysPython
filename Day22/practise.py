import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/dataset/53/iris'

response = requests.get(url)
status = response.status_code
print(status)
content = response.content  # we get all the content from the website

soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())

tables = soup.find_all('table', )
print(tables)

table = tables[0]  # the result is a list, we are taking out data from it
for td in table.find('tbody').find_all('tr'):
    print(td)
