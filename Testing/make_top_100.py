from bs4 import BeautifulSoup
import json
import requests


def make_top_100():

    with open(r'D:\Coding\Python\OSRS Stock Trader\all_items.json') as data_file:
        all_items = json.load(data_file)

        r = requests.get(r'http://services.runescape.com/m=itemdb_oldschool/top100?list=0')
        web_data = r.text
        soup = BeautifulSoup(web_data, 'html5lib')
        top_100_items = []
        for row in soup.find_all('span'):
            item_name = ''.join(row.findAll(text=True))
            for item in all_items:
                if item_name == item['name']:
                    top_100_items.append({'id': item['id'],
                                          'name': item['name']})
                    continue

    with open(r'D:\Coding\Python\OSRS Stock Trader\top_100.json', 'w') as outfile:
        json.dump(top_100_items, outfile, indent=4)


make_top_100()