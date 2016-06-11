import requests
from bs4 import BeautifulSoup

baseUrl = "http://www.nairaland.com"

page = requests.get(baseUrl)

data = page.text

soup = BeautifulSoup(data, "html.parser")

for item in soup.find_all("td", class_="featured w"):
    print item
