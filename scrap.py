from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")


a = soup.find_all("table")[1]

b = a.find_all("th")

print(b)
