from binance.client import Client
import pandas as pd
import asyncio
import time
import keys
from binance.spot import Spot

# async def main():
#     client = await AsyncClient.create(keys.api_key, keys.secret_kay)
#
#
# if __name__ == "__main__":
#
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


#You have to past your binance keys to file keys.py, or just open file start.bat
client = Client(keys.api_key, keys.secret_kay)


#function's get historickal data
def data_klines(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + 'min ago UTC'))
    frame = frame.iloc[:,:6]
    frame = frame.set_axis(['Time', 'Open', 'High', 'Low', 'Close', 'Volume'], axis=1, inplace=False)
    print(frame.columns)
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit = 'ms')
    frame = frame.astype(float)
    return frame

#function's 

BTCUSDT_H = data_klines('BTCUSDT', '1m', '120')
ETHUSDT_H = data_klines('ETHUSDT', '1m', '120')

df = BTCUSDT
print(df)
