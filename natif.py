import os
import csv 
import urllib.request

file_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv"
file_path = 'data.csv'

if os.path.exists(file_path) == False:
   urllib.request.urlretrieve(file_url, file_path)

# read the data with csv into list 'sales'
sales = []
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')

    for row in csv_reader:
        sales.append(row)

qtes = {}
for row in range(1, len(sales)):
    key = sales[row][1]
    if (key in qtes) == False:
        qtes[key] = 0

    qtes[key] += int(sales[row][3])

#debug 
#print(qtes)

produit_plus_vendu = max(qtes, key=qtes.get)
produit_moins_vendu = min(qtes, key=qtes.get)

print(f"Le produit le plus vendu est : {produit_plus_vendu} ({qtes[produit_plus_vendu]} unités)")
print(f"Le produit le moins vendu est : {produit_moins_vendu} ({qtes[produit_moins_vendu]} unités)")