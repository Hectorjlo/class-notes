import pandas as pd

genes = {
    'GeneID': ['b0001', 'b0002', 'b0003'],
    'Nombre': ['thrL', 'thrA', 'thrB'],
    'Función': ['regulador', 'enzima', 'enzima'],
    'Longitud': [117, 2340, 1461]
}
df_genes = pd.DataFrame(genes)

print(df_genes)

f = df_genes[(df_genes['Función'] == 'enzima') & (df_genes['Longitud'] > 1000)]['GeneID']
print(f)

df_genes['Es_largo'] = df_genes['Longitud'] > 1000
print(df_genes)


