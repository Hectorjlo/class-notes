import pandas as pd

df = pd.read_csv('data\pandas_\genes.csv')

renamed_df = df.rename(columns={'Función': 'Tipo funcional'})

estandarized_df = df.replace({'Función': {'enzima': 'enzima metabolica'}})

not_expression_df = df.drop(columns=['Expresión'], inplace=False, axis=1)

df['Longitud'] = df['Longitud'].astype(float)

df['Clasificacion'] = df['Longitud'].apply(lambda length: 'Largo' if length > 1000 else 'Corto')

df['Nivel de expresion'] = df['Expresión'].apply(lambda expression_level: 'Sobreexpresado' if expression_level > 35 else 'Subexpresado')

new_df = df.assign(Log_Expression =lambda x: x['Expresión'].apply(lambda sqrt: round(sqrt ** .5, 2)))

df['Expresion genica'] = df['Expresión'].apply(lambda genic_expression: 'Alta' if genic_expression > 40 else ('Media' if genic_expression > 15 else 'Baja') )

df['Tipo'] = df['Función'].apply(lambda funtion: 'Metabolico' if funtion.lower() == 'enzima' else 'Otro')

df['Gene_ID_modified'] = df['GeneID'].apply(lambda name: f'eco_{name}')

print(renamed_df)
print(estandarized_df)
print(not_expression_df)
print(new_df)
print(df)