import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://rsf.org/en/index?year="

for year in ["2021", "2022"]:
    url = URL + year
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.select("table")[0]
    index_df = pd.read_html(str(table))[0]
    index_df.to_csv(f'./datasets/press_{year}.csv', index=False)