##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd
import numpy as np

df = pd.read_csv('tbl1.tsv',  # el archivo
                    sep = '\t',         # separador de campos
                    thousands = None,  # separador de miles para números
                    decimal = '.')  

df = df.sort_values('_c4')
x = df.groupby('_c0')['_c4'].apply(lambda x: ','.join(map(str, x))).reset_index()
x = x.rename(index=str, columns={"_c4": "lista"})
print(x)
