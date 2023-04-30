import csv
import json
from urllib.request import urlopen
from pandas import *

file = open('average_yearly_temperatures_celcius_1901-2021_world.csv', newline='')
csv_data = read_csv("average_yearly_temperatures_celcius_1901-2021_world.csv")
response = urlopen('https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson')

data = json.loads(response.read())

type(file)

csvreader = csv.reader(file)

csv_country_names = []
csv_country_names = csv_data['country'].tolist()
#print(csv_country_names)
#print(csv_country_names) #deleting the "year" column from our countries array

rows = []
for row in csvreader:
        rows.append(row)

matched = []
not_matched = []
#for i in range(len(csv_country_names)):
    #for j in data['features']:
   #     if(j['properties']['name'])==(csv_country_names[i]):
            #print(csv_country_names[i] + " ")

for j in data['features']:
    for i in range(len(csv_country_names)):
        if(j['properties']['name'])==(csv_country_names[i]):
             matched.append(j['properties']['name'])
    if j['properties']['name'] not in matched: 
        not_matched.append(j['properties']['name'])
print((not_matched))


#for i in data['features']:
    #print(i['properties']['name'])


file.close()