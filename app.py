import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

print("\n--- données---")
print(données)

données['ca'] = données['qte'] * données['prix']

mediane_ca_produit = données.groupby('produit')['ca'].median().reset_index()
print("\n--- Mediane CA ---")
print(mediane_ca_produit)

moyenne_ca_produit = données.groupby('produit')['ca'].mean().reset_index()
print("\n--- Moyenne CA ---")
print(moyenne_ca_produit)

mediane_qte_produit = données.groupby('produit')['qte'].median().reset_index()
print("\n--- Mediane qte ---")
print(mediane_qte_produit)

moyenne_qte_produit = données.groupby('produit')['qte'].mean().reset_index()
print("\n ---Moyenne qte ---")
print(moyenne_qte_produit)

ecart_type = données.groupby('produit')['qte'].std().reset_index()
print("\n ---Écart-type---")
print(ecart_type)

variance = données.groupby('produit')['qte'].var().reset_index()
print("\n--- Variance ---")
print(variance)

ca_produit = données.groupby('produit')['ca'].sum().reset_index()
print("\n--- ca_produit ---")
print(ca_produit)

figure = px.pie(ca_produit, values='ca', names='produit', title='CA par produit')
figure.write_html('ca-par-produit.html')

ventes_produit = données.groupby('produit')['qte'].sum().reset_index()

print("\n--- ventes_produit ---")
print(ventes_produit)

figure = px.pie(ventes_produit, values='qte', names='produit', title='Ventes par produit')
figure.write_html('vente-par-produit.html')

