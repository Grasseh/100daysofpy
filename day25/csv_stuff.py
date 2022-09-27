import csv

with open('csv.csv') as file:
    data = csv.reader(file)
    for row in data:
        print(row[1])

import pandas
data = pandas.read_csv('csv.csv')
print(data)

filtered_data = data[data['my first column'] == 12]

data_dict = {
    'cola': ['Gray', 'Yelo'],
    'values': [1, 2]
}

df = pandas.DataFrame(data_dict)
df.to_csv('stuff.csv')
