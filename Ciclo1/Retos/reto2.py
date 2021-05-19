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

etnias = ['afrodescendiente', 'indigena', 'raizal',
          'palenquero', "gitano", 'sinreconocimiento']

estratos = [1, 2, 3, 4, 5, 6]

# ejecutamos las validaciones según el numero de aplicantes
for i in range(cantidad_aplicantes):
    etnia = input()
    estrato = int(input())
    salario = int(input())

    # Si se ingresa un dato que no esta en las listas se reinicia el loop con el dato siguiente
    if etnia not in etnias or estrato not in estratos:
        continue

    puntaje = 0
    pEtnia = 0
    pEstrato = 0
    pSalario = 0
    smlv = 908526

    # Verificacion de la etnia
    if etnia == 'afrodescendiente':
        pEtnia = 8
        afrodescendiente += 1
    if etnia == 'indigena':
        pEtnia = 10
        indigena += 1
    if etnia == 'raizal':
        pEtnia = 12
        raizal += 1
    if etnia == 'palenquero':
        pEtnia = 14
        palenquero += 1
    if etnia == 'gitano':
        pEtnia = 16
        gitano += 1
    if etnia == 'sinreconocimiento':
        pEtnia = 0
        sinreconocimiento += 1

    # Verificacion del estrato
    if estrato == 1:
        pEstrato = 20
    if estrato == 2:
        pEstrato = 16
    if estrato == 3:
        pEstrato = 12
    if estrato == 4:
        pEstrato = 8
    if estrato == 5 or estrato == 6:
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

    puntaje = pEtnia + pEstrato + pSalario
    if puntaje >= 50:
        continua += 1

print(continua)
print("sin reconocimiento", sinreconocimiento)
print("afrodescendiente", afrodescendiente)
print("indigena", indigena)
print("raizal", raizal)
print("palenquero", palenquero)
print("gitano", gitano)
