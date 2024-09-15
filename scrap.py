from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from requests_html import AsyncHTMLSession, HTMLSession

asession = AsyncHTMLSession()
session = HTMLSession()


# async def get_data():
#     url = await asession.get(
#         "https://poe.ninja/economy/settlers/skill-gems?level=1&gemType=Transfigured"
#     )
#     print(url.html.links)


# res = asession.run(get_data)


r = session.get(
    "https://poe.ninja/economy/settlers/skill-gems?level=1&gemType=Transfigured"
)
# print(res)
r.html.render()
page = r.html.text
# page = requests.get(url)

soup = BeautifulSoup(page, "html")
print(soup)
# soup = r.html.find('th')
# print(soup)
# cwd = os.getcwd()
# path = cwd + "/new.csv"

# table = soup.find_all("table")
#
# table_titles = table.find_all("th")
#
# column_titles = [title.text.strip() for title in table_titles]


# print(column_titles)

# df = pd.DataFrame(columns=column_titles)

# column_data = table.find_all("tr")


# for r in column_data[2:]:
#     row_data = r.find_all("td")
#     row = [data.text.strip() for data in row_data]
#     # print(row)
#     length = len(df)
#     df.loc[length] = row

# df.to_csv(path)
