##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
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
    x=0
    for line in text:
        if line[0] == letra:
            x = x+int(line[1])
    print('{},{}'.format(letra,x))