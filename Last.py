import requests
from bs4 import BeautifulSoup

usd = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
soup = BeautifulSoup(usd.text, "html.parser")

usdt = soup.find("td", string="USD").find_next("td", {"data-label": "Офіційний курс"}).text
print(f"Курс USD: {usdt}")