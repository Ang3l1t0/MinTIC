import csv
from operator import itemgetter

# declaraciones
capital = input()
continua = 0
afrodescendiente = 0
indigena = 0
raizal = 0
palenquero = 0
gitano = 0
sinreconocimiento = 0
smlv = 908526
ingresos = []

# abrimos el archivo data.csv con permisos de lectura
with open("./data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in (reader):
        if row[2] == capital and row[7] == "1":
            etnia = row[4]
            ingreso = int(row[6])
            ingresos.append(ingreso)

            # conteo por etnia
            if etnia == 'afrodescendiente':
                afrodescendiente += 1
            elif etnia == 'indigena':
                indigena += 1
            elif etnia == 'raizal':
                raizal += 1
            elif etnia == 'palenquero':
                palenquero += 1
            elif etnia == 'gitano':
                gitano += 1
            elif etnia == 'sin reconocimiento':
                sinreconocimiento += 1
            continua += 1

ingresos = sorted(ingresos)
promedio = sum(ingresos)/len(ingresos)
resultados = [
    ("sin reconocimiento", sinreconocimiento),
    ("raizal", raizal),
    ("palenquero", palenquero),
    ("indigena", indigena),
    ("gitano", gitano),
    ("afrodescendiente", afrodescendiente)
]
print(continua)
print('{} {} {:.2f}'.format(ingresos[0], ingresos[-1], promedio))
for k, v in sorted(resultados, key=itemgetter(1, 0), reverse=True):
    if v != 0:
        print(k, v)
