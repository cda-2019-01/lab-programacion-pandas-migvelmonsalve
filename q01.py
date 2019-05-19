##
## Imprima la suma de la segunda columna.
##
text = []
with open('data.csv', 'rt') as f:
    text += f.readlines()

text = [line.replace('\t',',') for line in text]
text = [line.split(',') for line in text]

x = 0

for line in text:
    x = x + int(line[1])

print(x)