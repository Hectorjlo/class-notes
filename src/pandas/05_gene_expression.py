import pandas as pd

df = pd.read_csv("data/pandas_/expresion_genica.tsv", sep='\t', header=0)

overexpressed_df = df[(df['cond1'] > 1000) & (df['cond2'] > 1000) & (df['cond3'] > 1000)]
print(overexpressed_df)