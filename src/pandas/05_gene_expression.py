import pandas as pd

df = pd.read_csv("data/pandas_/expresion_genica.tsv", sep='\t', header=0)

overexpressed_df = df[(df['cond1'] > 1000) & (df['cond2'] > 1000) & (df['cond3'] > 1000)]

overexpressed_df['means'] = overexpressed_df[['cond1', 'cond2', 'cond3']].mean(axis=1)

overexpressed_df_sorted = overexpressed_df.sort_values(by='means', ascending=False)




print(overexpressed_df)

print(overexpressed_df_sorted)

overexpressed_df_sorted.to_csv('results/pandas_/overexpressed_df_sorted.csv', sep=',', index=False, header=True)
