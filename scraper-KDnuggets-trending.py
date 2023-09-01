import requests
from bs4 import BeautifulSoup

url = "https://www.kdnuggets.com/"
res = requests.get(url)
htmlData = res.content


# Parse the html
parsedData = BeautifulSoup(htmlData, 'html.parser')
parsedData.prettify()

soup = BeautifulSoup("<h1> Welcome to KDnuggets! </h1>", "html.parser")
print(type(soup))