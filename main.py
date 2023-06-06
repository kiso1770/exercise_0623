# cd C:\Users\kiso1\OneDrive\Рабочий стол\Забдание
# python main.py
# python check_ETFUSDT.py

from binance.client import Client
import pandas as pd
import json
import requests
import datetime
import time
# defining key/request url
link = "https://api.binance.com/api/v3/ticker/price?symbol="
symbols = ['ETHUSDT', 'BTCUSDT']
df = []

# requesting data from url
def get_price(symbol):
    price = requests.get(link+symbol)
    price = price.json()
    return price

def check_price():
        row = int(round([datetime.datetime.now().timestamp()),
         get_price('ETHUSDT')['price'],
         get_price('BTCUSDT')['price']]
        df.append(row)
        return 0

while True:
    check_price()
    if len(df) >= 1000:
        print(df[0][0])
        break #chenge on 