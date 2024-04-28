import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_currencies(interval1: list[int], interval2: list[int], cur):
    url = f"https://www.finmarket.ru/currency/rates/?id=10148&pv=1&cur={cur}&bd={interval1[2]}&bm={interval1[1]}&by={interval1[0]}&ed={interval2[2]}&em={interval2[1]}&ey={interval2[0]}&x=48&y=13#archive"
    data = requests.get(url)
    data.encoding = '1251'

    soup = BeautifulSoup(data.text, 'html.parser')
    table = soup.find('tbody')
    rows = table.find_all('tr')
    neighborhood_data = []

    for row in rows:
        columns = row.find_all('td')
        row_data = [col.get_text(strip=True) for col in columns]
        neighborhood_data.append(row_data)

    df = pd.DataFrame(neighborhood_data, columns=[ "date", "amount", "rate", "changes"])

    return df
