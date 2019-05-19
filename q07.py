##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
##
##
text = []
with open('data.csv', 'rt') as f:
        text += f.readlines()
        
text = [line.replace('\t',',') for line in text]
text = [line.split(',') for line in text]
text2 = [line[1] for line in text]
text3 = list(set(text2))
text3.sort()
for letra in text3:
    x=[]
    for line in text:
        if line[1] == letra:
            x.append(line[0])
    y = (letra,x)
    print(y)