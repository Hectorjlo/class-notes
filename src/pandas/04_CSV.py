import pandas as pd

f = pd.read_csv('data\pandas_\genes.gff3', sep='\t', comment='#', header=None)

print(f)

