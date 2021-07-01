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
            # guardamos los valores de los ingresos en una lista
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
            # Conteo de los que continuan
            continua += 1

# ordenamos nuestra lista de ingresos
ingresos = sorted(ingresos)
# obtenemos el promedio de los valores de la lista ingresos
promedio = sum(ingresos)/len(ingresos)
# Lista de tuplas de las etnias esta declarada en orden alfabetico para que se respete la jerarquia
resultados = [
    ("afrodescendiente", afrodescendiente),
    ("gitano", gitano),
    ("indigena", indigena),
    ("palenquero", palenquero),
    ("raizal", raizal),
    ("sin reconocimiento", sinreconocimiento)
]
print(continua)
# el valor minimo es el primer valor de la lista y el mas alto el ultimo porque tya esta ordenada
print('{} {} {:.2f}'.format(ingresos[0], ingresos[-1], promedio))
# imprimo las etnias ordenadas por valor
for k, v in sorted(resultados, key=itemgetter(1), reverse=True):
    if v != 0:
        print(k, v)
