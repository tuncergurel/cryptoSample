import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sql_connection import sqlConnect as sqlConnect

def selectCoins(first,sec):
    cur = sqlConnect()
    query = """select * from cryptocurrency"""

    cur.execute(query)
    data = cur.fetchall()

    df = pd.read_sql_query(query,cur.connection)

    crypto = df.loc[df['coin_symbol'] == first]
    seccrypto = df.loc[df['coin_symbol'] == sec]
    time = crypto['last_updated']

    plt.figure(figsize=(20, 5))
    plt.plot(time, crypto['coin_USD_price'], color='red', marker='o')
    plt.plot(time, seccrypto['coin_USD_price'], color='blue', marker='+')
    plt.xlabel('Time')
    plt.ylabel('Prices')
    plt.grid(True)
    plt.show()


def main():
    first = 'BUSD'
    sec = 'UST'
    selectCoins(first,sec)

main()