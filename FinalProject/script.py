import csv
import json
from urllib.request import urlopen
from pandas import *

file = open('average_yearly_temperatures_celcius_1901-2021_world.csv', newline='')
csv_data = read_csv("average_yearly_temperatures_celcius_1901-2021_world.csv")
response = urlopen('https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson')

data = json.loads(response.read())

type(file)

#csv file object
csvreader = csv.reader(file)

#making array of country names
csv_country_names = []
csv_country_names = csv_data['country'].tolist()

#making array of row objects
rows = []
for row in csvreader:
        rows.append(row)


matched = []
not_matched = []

#matching csv names to json names
for j in data['features']:
    for i in range(len(rows)):
        if(j['properties']['name'])==(rows[i][0]):
             matched.append(j['properties']['name'])
             startingYear = 1901
             #print(rows[i][0]) 

#populate array containing countries in csv that are not matched to world.geo.json
for i in range(len(csv_country_names)):
        if csv_country_names[i] not in matched: 
            not_matched.append(csv_country_names[i])
            
#remove countries not in world.geo.json from rows array containing all csv countries            
for j in not_matched:            
    for i in rows:
        if(j)==(i[0]):
            rows.remove(i)

rows.pop(0) #remove header row

#setting temp190xx to be a property in the world.geo.json features
for j in data['features']:
    jsonCountry = j['properties']['name']
    for i in rows:
        if(i[0] == jsonCountry):
            startingYear = 1901
            for k in range(122):
                if k != 0: 
                    tempYear = "temp" + str(startingYear)
                    j['properties'][tempYear] = i[k]
                    startingYear = startingYear + 1

json_file = json.dumps(data)
print(json_file)

file.close()

with open('final_world.geo.json', 'w') as _f:
    json.dump(json_file, _f)

