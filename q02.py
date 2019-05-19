##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
text = []
with open('data.csv', 'rt') as f:
        text += f.readlines()
        
text = [line.replace('\t',',') for line in text]
text = [line.split(',') for line in text]
text2 = [line[0] for line in text]
text3 = list(set(text2))
text3.sort()
for letra in text3:
    print('{},{}'.format(letra,text2.count(letra)))
