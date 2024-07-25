import json
from urllib.request import urlopen

with urlopen("https://api.exchangerate-api.com/v4/latest/USD") as response:
    source = response.read()
# print(source)
data = json.loads(source)
# print(data)
# print(data.keys())
# print(len(data['rates']))

# print(json.dumps(data,indent=2,sort_keys=True))
val = data['rates'].keys()
print("Available currency codes:","\n".join(val))
choice =input("enter the currency:").upper()

if choice in data['rates']:
    convert = float(input("how many dollars you want to convert in {choice}?:"))
    print(convert * data['rates'][choice])

else:
    raise KeyError("ERROR 404 try again!")






