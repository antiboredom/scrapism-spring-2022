import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.amazon.com/s?k=blue+lives+matter&page=3&crid=30EDJ17SBJ8DH&qid=1648597754&sprefix=blue+lives+mater%2Caps%2C100&ref=sr_pg_2")
html = response.text
soup = BeautifulSoup(html, "html.parser")

titles = soup.select("h2")
for t in titles:
    print(t.text.strip())