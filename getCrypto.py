import requests
from sql_connection import sqlConnect as sql
import time
import datetime
import coins_dict as dc

cur = sql()
url = 'url'

params = {
    'start': '1',
    'limit': '50',
    'convert': 'USD'
}

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'key'
}

count = 1

while True:
    json = requests.get(url, params=params, headers=headers).json()
    coins = json["data"]

    for x in coins:

        coin_symbol = x['symbol']
        coin_no = dc.coins[coin_symbol]
        coin_name = x['slug']
        coin_USD_price = x['quote']['USD']['price']
        coin_percent_change_24h = x['quote']['USD']['percent_change_24h']
        coin_percent_change_7d = x['quote']['USD']['percent_change_7d']
        coin_market_cap = x['quote']['USD']['market_cap']
        coin_volume_24h = x['quote']['USD']['volume_24h']
        coin_circulating_supply = x['circulating_supply']
        last_updated = x['last_updated']
        

        cur.execute('insert into cryptocurrency(coin_no,coin_symbol,coin_name,coin_USD_price,coin_percent_change_24h,'
            'coin_percent_change_7d,coin_USD_market_cap,coin_USD_volume_24h,coin_circulating_supply,last_updated) '
            'values(?,?,?,?,?,?,?,?,?,?)',
            (coin_no,coin_symbol,coin_name,coin_USD_price,coin_percent_change_24h,coin_percent_change_7d,coin_market_cap,
             coin_volume_24h,coin_circulating_supply,last_updated))
        cur.commit()

    print("{} datas added to Mssql at {}".format(count,datetime.datetime.now()))
    count += 1
    time.sleep(1800)


