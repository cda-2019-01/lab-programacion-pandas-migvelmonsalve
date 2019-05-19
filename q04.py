##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

df = pd.read_csv('tbl1.tsv',  # el archivo
                    sep = '\t',         # separador de campos
                    thousands = None,  # separador de miles para números
                    decimal = '.')

x = df['_c4'].unique()
x = [line.upper() for line in x]
x.sort()
print(x)

