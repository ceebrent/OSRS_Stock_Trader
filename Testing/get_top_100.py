import json


def top_100_dict_gen():

    with open(r'D:\Coding\Python\OSRS_Stock_Trader\top_100.json') as data_file:
        items = json.load(data_file)
    return items
    # print(items)
    # for item in items:
    #     print(item.get('id'))
