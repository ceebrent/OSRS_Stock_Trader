import requests
import datetime

r = requests.get(
    r'http://services.runescape.com/m=itemdb_oldschool/api/graph/4151.json')

print(r.text)
s = "1487030400000"
t = datetime.datetime.fromtimestamp(float(1478217600000) / 1000)

fmt = "%Y-%m-%d %H:%M:%S"
print(t.strftime(fmt))