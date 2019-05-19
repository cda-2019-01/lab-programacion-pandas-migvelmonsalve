##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
text = []
with open('data.csv', 'rt') as f:
        text += f.readlines()
        
text = [line.replace('\t',',') for line in text]
text = [line.split(',') for line in text]
text2 = [line[0] for line in text]
text4 = [line[1] for line in text]
text3 = list(set(text2))
text3.sort()
for letra in text3:
    x=int(text4[text2.index(letra)])
    y=int(text4[text2.index(letra)])
    for line in text:
        if line[0] == letra:
            if int(line[1]) > x:
                x = int(line[1])
            elif int(line[1]) < y:
                y = int(line[1])
    print('{},{},{}'.format(letra,x,y))