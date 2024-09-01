from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

url = "https://en.wikipedia.org/wiki/2024_Summer_Paralympics"
cwd = os.getcwd()

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")

table = soup.find_all("table")[0]

more = table.find_all("a")

print(more)
