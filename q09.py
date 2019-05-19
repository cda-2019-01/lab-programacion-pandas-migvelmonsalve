##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
import numpy as np

df = pd.read_csv('tbl0.tsv',  # el archivo
                    sep = '\t',         # separador de campos
                    thousands = None,  # separador de miles para números
                    decimal = '.')  

df = df.sort_values('_c2')
x = df.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, x))).reset_index()
x = x.rename(index=str, columns={"_c2": "lista","_c1": "_c0"})
print(x)

