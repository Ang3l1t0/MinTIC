from operator import itemgetter

postulados = int(input())

# declaración de variables
etnias = ["afrodescendiente", "indigena", "raizal",
          "palenquero", "gitano", "sin reconocimiento"]
estratos = [1, 2, 3, 4, 5, 6]
continuan = 0
noContinua = 0
error = 0
sinreconocimiento = 0
afrodescendiente = 0
indigena = 0
raizal = 0
palenquero = 0
gitano = 0

for personas in range(postulados):
    informacion = input().split(",")
    etnia = informacion[0]
    estrato = int(informacion[1])
    ingreso = int(informacion[2])

    if etnia not in etnias or estrato not in estratos:
        error += 1
        continue

    # variables declaradas
    puntosEtnia = 0
    puntosEstrato = 0
    puntosIngreso = 0
    total = 0
    smlv = 908526

    # Verificacion de la etnia
    if etnia == "afrodescendiente":
        puntosEtnia = 8
        afrodescendiente += 1
    elif etnia == "indigena":
        puntosEtnia = 10
        indigena += 1
    elif etnia == "raizal":
        puntosEtnia = 12
        raizal += 1
    elif etnia == "palenquero":
        puntosEtnia = 14
        palenquero += 1
    elif etnia == "gitano":
        puntosEtnia = 16
        gitano += 1
    elif etnia == "sin reconocimiento":
        puntosEtnia = 0
        sinreconocimiento += 1

    # Verificacion de estrato
    if estrato == 1:
        puntosEstrato = 20
    elif estrato == 2:
        puntosEstrato = 16
    elif etnia == 3:
        puntosEstrato = 12
    elif estrato == 4:
        puntosEstrato = 8
    elif estrato == 5 or estrato == 6:
        puntosEstrato = 0

    # Verificacion de los ingresos
    if ingreso < smlv:
        puntosIngreso = 30
    elif ingreso < (2 * smlv):
        puntosIngreso = 18
    elif ingreso < (smlv * 4):
        puntosIngreso = 14
    elif ingreso < (smlv * 5):
        puntosIngreso = 8
    elif ingreso >= (smlv * 5):
        puntosIngreso = 0

    # print(puntosEtnia, puntosEstrato, puntosIngreso)
    # sumatoria de puntajes
    total = puntosEtnia + puntosEstrato + puntosIngreso
    # print(total)

    if total >= 50:
        continuan += 1  # continuan = continuan + 1
    else:
        noContinua += 1

print(continuan, noContinua, error)
resultados = [
    ("sin reconocimiento", sinreconocimiento),
    ("afrodescendiente", afrodescendiente),
    ("indigena", indigena),
    ("raizal", raizal),
    ("palenquero", palenquero),
    ("gitano", gitano)
]

for key, value in sorted(resultados, key=itemgetter(1,0), reverse=True):
    print(key, value)