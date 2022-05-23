import pandas as pd
import numpy as np
import csv
def importData():
    df = pd.read_csv('newRappi3.csv', sep=",")
    data = df.to_numpy()
    return data


data = importData()

#print(data)
index = {}
cats = np.zeros((10, int(data.shape[0])))

header = []
index['Hamburguesas'] = 0
#print(cats)
idx = 0



for row in data:
    if row[2] not in index:
        index[row[2]] = index[max(index, key=index.get)] + 1
    header.append(row[3])
    cats[:,idx] = cats[:, idx - 1]
    cats[index[row[2]]][idx] = cats[index[row[2]]][idx - 1] + row[1]
    idx += 1

print(index)
with open('cats.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    # write multiple rows
    writer.writerows(cats)