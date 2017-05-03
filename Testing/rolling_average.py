import json
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import requests
matplotlib.style.use('ggplot')

data = requests.get(
    r'http://services.runescape.com/m=itemdb_oldschool/api/graph/810.json')


with open(r'D:\Coding\Python\OSRS Stock Trader\test_return.json') as data_file:
    json = data.json()
    df = pd.DataFrame.from_dict(json)
    df.index.name = 'Date'
    df.reset_index(inplace=True)
    df['Date'].str.decode("utf-8")
    df['Date'] = df['Date'].astype(np.int64)
    df['Date'] = df['Date']/1000
    df['Date'] = pd.to_datetime(df['Date'].astype(int), unit='s')

    df_60 = df.ix[120:]

    daily_df = df_60['daily']
    # daily_df.reset_index(inplace=True)
    roll_df = df.ix[117:]['daily'].rolling(center=False, window=4).mean()
    roll_df.name = '4-Day Rolling'
    last_dailey = daily_df.iloc[-1]
    last_roll = roll_df.iloc[-1]

    print(last_dailey, last_roll)
    ax1 = daily_df.plot()
    roll_df.plot()
    lines, labels = ax1.get_legend_handles_labels()
    ax1.legend(lines, labels, loc='best')
    plt.show()