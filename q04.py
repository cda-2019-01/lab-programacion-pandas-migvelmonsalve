##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
text = []
with open('data.csv', 'rt') as f:
        text += f.readlines()
        
text = [line.replace('\t',',') for line in text]
text = [line.split(',') for line in text]
text = [z+[z[2].split('-')[1]] for z in text]
text2 = [line[-1] for line in text]
text3 = list(set(text2))
text3.sort()
for letra in text3:
    print('{},{}'.format(letra,text2.count(letra)))