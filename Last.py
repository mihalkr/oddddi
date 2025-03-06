import requests
responce = requests.get("https://bank.gov.ua/ua/markets/")

from bs4 import BeautifulSoup

ton = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
soup = BeautifulSoup(ton.text, features="html.parser")
usdt = soup.find("td", string="USD").find_next("td", {"data-label": "Офіційний курс"}).text
print(f"Курс USD: {usdt}")