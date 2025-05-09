import pandas as pd

data = {
    'Gene': ['thrL', 'thrA', 'thrB'],
    'Longitud' : [117, 2340, 1461]
}

df = pd.DataFrame(data)

print(df)