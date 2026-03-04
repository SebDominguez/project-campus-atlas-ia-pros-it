# Requêtes SQL

## 3.a. Le chiffre d'affaires total
```sql
Select sum(prix * qte) AS ca_total
from ventes;
```
Résultat:

|ca_total|
|--------|
|44825   |


## 3.b. Les ventes par produit
```sql
SELECT produit, SUM(qte * prix) AS ca_produit
FROM ventes
GROUP BY produit;
```
Résultat:

|produit  |ca_produit|
|---------|----------|
|Produit A|17500     |
|Produit B|15825     |
|Produit C|11500     |

## 3.c. Les ventes par région

```sql
SELECT region, SUM(qte*prix) ca_region
FROM ventes
GROUP BY region;
```

Résultat:

|region   |ca_region|
|---------|---------|
|Nord     |20725    |
|Sud      |24100    |

## 5.a Chiffre d’affaires par produit et le volume des ventes par
produit
5.a.i Moyenne:
```python3
moyenne_ca_produit = données.groupby('produit')['ca'].mean().reset_index()
moyenne_qte_produit = données.groupby('produit')['qte'].mean().reset_index()

--- Moyenne CA ---
     produit           ca
0  Produit A  1250.000000
1  Produit B  1217.307692
2  Produit C   958.333333

---Moyenne qte ---
     produit         qte
0  Produit A  125.000000
1  Produit B   81.153846
2  Produit C   47.916667
```
5.a.ii Médiane
```python3
mediane_ca_produit = données.groupby('produit')['ca'].median().reset_index()
mediane_qte_produit = données.groupby('produit')['qte'].median().reset_index()

--- Mediane CA ---
     produit      ca
0  Produit A  1225.0
1  Produit B  1200.0
2  Produit C   900.0

--- Mediane qte ---
     produit    qte
0  Produit A  122.5
1  Produit B   80.0
2  Produit C   45.0
```
 ## 6 Code natif qui permet de trouver le produit le plus vendu et le moins vendu 
 
 ```python3
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
 ```
 ## 7 Graphiques
 a. Ventes par produit:
 [Voir le graphique des ventes par produit](./vente-par-produit.html)
 b. Chiffre d'affaires par produit:
 [Voir le graphique du CA par produit](./ca-par-produit.html)