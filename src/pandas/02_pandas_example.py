import pandas as pd
data = {
    'Nombre': ['Ana', 'Luis', 'Sofía'],
    'Edad': [28, 34, 22],
    'Ciudad': ['CDMX', 'Guadalajara', 'Monterrey']
}
df = pd.DataFrame.from_dict(data, orient='index')
print(df)


df[(df['Edad'] > 25) & (df['Ciudad'] == 'CDMX')]

