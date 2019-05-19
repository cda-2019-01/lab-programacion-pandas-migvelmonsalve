##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np

df = pd.read_csv('tbl0.tsv',  # el archivo
                    sep = '\t',         # separador de campos
                    thousands = None,  # separador de miles para números
                    decimal = '.')  

df['suma'] = df['_c0'].astype(int) + df['_c2'].astype(int)
print(df)
