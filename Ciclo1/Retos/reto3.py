import operator
# Numero de candidatos que se ingresaran
cantidad_aplicantes = int(input())

# Declaracion
continua = 0
afrodescendiente = 0
indigena = 0
raizal = 0
palenquero = 0
gitano = 0
sinreconocimiento = 0
error = 0
noContinua = 0
smlv = 908526

etnias = ['afrodescendiente', 'indigena', 'raizal',
          'palenquero', "gitano", 'sin reconocimiento']

estratos = [1, 2, 3, 4, 5, 6]

# ejecutamos las validaciones según el numero de aplicantes
for i in range(cantidad_aplicantes):
    info = input().split(',')
    etnia = info[0]
    estrato = int(info[1])
    salario = int(info[2])
    # Si se ingresa un dato que no esta en las listas se reinicia el loop con el dato siguiente
    if etnia not in etnias or estrato not in estratos:
        error += 1
        continue

    # declaración de variables que cambian por ciclo
    puntaje = 0
    pEtnia = 0
    pEstrato = 0
    pSalario = 0

    # Verificacion de la etnia
    if etnia == 'afrodescendiente':
        pEtnia = 8
        afrodescendiente += 1
    elif etnia == 'indigena':
        pEtnia = 10
        indigena += 1
    elif etnia == 'raizal':
        pEtnia = 12
        raizal += 1
    elif etnia == 'palenquero':
        pEtnia = 14
        palenquero += 1
    elif etnia == 'gitano':
        pEtnia = 16
        gitano += 1
    elif etnia == 'sin reconocimiento':
        pEtnia = 0
        sinreconocimiento += 1

    # Verificacion del estrato
    if estrato == 1:
        pEstrato = 20
    elif estrato == 2:
        pEstrato = 16
    elif estrato == 3:
        pEstrato = 12
    elif estrato == 4:
        pEstrato = 8
    elif estrato == 5 or estrato == 6:
        pEstrato = 0

    # Verificacion del salario
    if salario / smlv < 1:
        pSalario = 30
    elif salario / smlv < 2:
        pSalario = 18
    elif salario / smlv < 4:
        pSalario = 14
    elif salario / smlv < 5:
        pSalario = 8
    elif salario / smlv >= 5:
        pSalario = 0

    # Sumatoria de los puntajes acumulados y validamos si continua o no
    puntaje = pEtnia + pEstrato + pSalario
    if puntaje >= 50:
        continua += 1
    else:
        noContinua += 1

print(continua, noContinua, error)

resultados = [
    ("sin reconocimiento", sinreconocimiento),
    ("afrodescendiente", afrodescendiente),
    ("gitano", gitano),
    ("raizal", raizal),
    ("palenquero", palenquero),
    ("indigena", indigena)
]

# ordenamos la tupla de mayor a menor, index 1 referencia a segundo elemento
resultados.sort(key=lambda x: x[1], reverse=True)

# recorremos el key value de cada tupla e imprimimos su valor
for k, v in resultados:
    print(k, v)
