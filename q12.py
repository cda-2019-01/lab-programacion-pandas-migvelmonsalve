##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

df = pd.read_csv('tbl2.tsv',  # el archivo
                    sep = '\t',         # separador de campos
                    thousands = None,  # separador de miles para números
                    decimal = '.') 

df2 = pd.read_csv('tbl0.tsv',  # el archivo
                    sep = '\t',         # separador de campos
                    thousands = None,  # separador de miles para números
                    decimal = '.') 

df = df.join(df2,how='left',on='_c0',lsuffix='_caller', rsuffix='_other')
df = df[['_c5a','_c2']]
df = df.sort_values('_c5a')
x = df.groupby('_c5a')['_c2'].sum()
print(x)

