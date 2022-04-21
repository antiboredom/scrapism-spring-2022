import requests
from bs4 import BeautifulSoup

response = requests.get("https://newyork.craigslist.org/search/bar")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
elements = soup.select(".result-heading")
for e in elements:
    print(e.text.strip())