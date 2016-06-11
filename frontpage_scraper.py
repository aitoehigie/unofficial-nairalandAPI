import requests
from bs4 import BeautifulSoup

baseUrl = "http://www.nairaland.com"

page = requests.get(baseUrl)

data = page.text

soup = BeautifulSoup(data, "html.parser")

def scrape():
    for item in soup.find_all("td", class_="featured w"):
        for link in item.find_all("a"):
            print link.text, ":", link.get("href")



if __name__ == "__main__":
    scrape()
