import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_data(crypto_id='ethereum', vs_currency='usd', days='max', interval='daily'):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart'
    params = {
        'vs_currency': vs_currency,
        'days': days,
        'interval': interval
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.drop('timestamp', axis=1, inplace=True)
    
    return df

df_eth = fetch_crypto_data()

df_eth.to_csv('ethereum_historical_prices.csv', index=False)

print("Ethereum data fetched and saved to ethereum_historical_prices.csv")
