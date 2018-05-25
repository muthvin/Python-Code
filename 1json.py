import json
from urllib.request import urlopen
'''
with open("data_file.json","r") as f:
    d = json.load(f)

for person in d['people']:
    print(person['name'])

new_string = json.dumps(d,indent =2,sort_keys=True)
print(new_string)
'''

#indent - function to display with specified indent
#sort_keys - helps to sort the list in alphabetic order


with urlopen("https://finance.yahoo.com/webservice/v1/symbols\
/allcurrencies/quote?format=json") as response:
    source = response.read()

data =json.loads(source)
#print(json.dumps(data,indent=2))
#print(len(data['list']['resources']))

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    print(name,price)
    
