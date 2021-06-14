import operator
etn = [[1, 1, 2, 1, 1, 3, 6],
       [6, 6, 1, 1, 1, 6, 5],
       [5, 4, 1, 2, 1, 3, 3]]
est= [[1, 2, 1, 4, 4, 1, 1],
       [4, 6, 1, 1, 2, 1, 3],
       [5, 3, 3, 2, 3, 6, 1]]
ing= [[400000, 1800000, 900000, 500000, 2000000, 1200000, 800000],
       [700000, 400000, 1200000, 456000, 456000, 2200000, 1250000],
       [4000000, 2000000, 1800000, 600000, 780000, 7000000, 400000]]

detnias = {"sin reconocimiento": 0, "afrodescendiente": 0, "indigena": 0, "raizal": 0, "palenquero": 0, "gitano": 0}
# Codigo para hallar las etnias que mas se presentaron por semana
mas= []
for f in range(len(etn)):
    for c in range(len(etn[f])):
        if etn[f][c] == 1:
            detnias["sin reconocimiento"] += 1
        elif etn[f][c] == 2:
            detnias["afrodescendiente"] += 1
        elif etn[f][c] == 3:
            detnias["indigena"] += 1
        elif etn[f][c] == 4:
            detnias["raizal"] += 1
        elif etn[f][c] == 5:
            detnias["palenquero"] += 1
        elif etn[f][c] == 6:
            detnias["gitano"] += 1
#print(detnias)
detnias_ordenado= sorted(detnias.items(), key=operator.itemgetter(1), reverse=True)
detnias_menos= min(detnias.items(), key=operator.itemgetter(1))
count = 1
for key, value in detnias_ordenado:
    if len(detnias) > count:
       print(key, end=',')
    else:
        print(key)
    count += 1
#print(detnias_ordenado)
print(detnias_menos[0])
