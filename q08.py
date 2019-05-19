##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

df = pd.read_csv('tbl0.tsv',  # el archivo
                    sep = '\t',         # separador de campos
                    thousands = None,  # separador de miles para números
                    decimal = '.')  

df['ano'] = df['_c3'].str.split('-').str[0]
print(df)
