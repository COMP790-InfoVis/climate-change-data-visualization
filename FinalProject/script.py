import csv
import json

file = open('average_yearly_temperatures_celcius_1901-2021_world.csv', newline='')
json_file = open('world.geo.json', newline='')

data = json.load(json_file)

type(file)

csvreader = csv.reader(file)

csv_country_names = []
csv_country_names = next(csvreader)
del csv_country_names[0] #deleting the "year" column from our countries array

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
print(matched)


#for i in data['features']:
    #print(i['properties']['name'])


file.close()