import csv
import json

file = open('annual-temp-data-2021.csv', newline='')
json_file = open('world.geo.json', newline='')

data = json.load(json_file)


type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
header

rows = []
for row in csvreader:
        rows.append(row)
rows

country_names = []

#print(header[0])
for i in range(len(rows)):
    for j in data['features']:
        if(j['properties']['name'])==(rows[i][0]):
            print(rows[i][0]+','+rows[i][1])
           

#print(rows[0])

#for i in data['features']:
    #print(i['properties']['name'])


file.close()
