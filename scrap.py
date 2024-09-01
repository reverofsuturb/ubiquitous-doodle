from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")

cwd = os.getcwd()
# path = cwd + "/new.csv"

table = soup.find_all("table")[0]

table_titles = table.find_all("th")[1:9]

column_titles = [title.text.strip() for title in table_titles]

# print(column_titles)

df = pd.DataFrame(columns=column_titles)

column_data = table.find_all("tr")


for r in column_data[2:]:
    row_data = r.find_all("td")
    row = [data.text.strip() for data in row_data]
    # print(row)
    length = len(df)
    df.loc[length] = row

df.to_csv(path)
