import csv
from operator import itemgetter
# declaracion
sinreconocimiento = 0
afrodescendiente = 0
indigena = 0
raizal = 0
palenquero = 0
gitano = 0

acumuladorIngreso = 0
continua = 0
lst_ingresos = []
# lst_etnias =[]

with open("./data.csv", "r") as file:  # organica
    reader = csv.reader(file)
    capital = input("")

    for row in reader:
        if row[2] == capital and row[7] == "1":  # busqueda "1" true "0" false
            etnia = row[4]
            ingresos = int(row[6])
            lst_ingresos.append(ingresos)  # ingresos
            continua += 1
            if etnia == "afrodescendiente":  # validacion de etnias
                afrodescendiente += 1
            elif etnia == "indigena":
                indigena += 1
            elif etnia == "raizal":
                raizal += 1
            elif etnia == "palenquero":
                palenquero += 1
            elif etnia == "gitano":
                gitano += 1
            elif etnia == "sin reconocimiento":
                sinreconocimiento += 1

lst_ingresos = sorted(lst_ingresos)  # para organizarl la lista de los ingresos
# funcion len(lst_ingresos) para contar elementos dentro de una lista
promedio = sum(lst_ingresos)/continua
lst_etnias = [
    ("afrodescendiente", afrodescendiente),
    ("indigena", indigena),
    ("gitano", gitano),
    ("palenquero", palenquero),
    ("raizal", raizal),
    ("sin reconocimiento", sinreconocimiento)]

print(continua)
# 2 decimales f=float - imprime el primer valor, ultimo valor de una lista, promedio
print("{} {} {:.2f}".format(lst_ingresos[0], lst_ingresos[-1], promedio))
for key, value in sorted(lst_etnias, key=itemgetter(1), reverse=True):
    if value != 0:
        print(key, value)
