cantidad = int(input('cantidad de personas a aplicar: '))

# declaración de variables
etnias = ['afrodescendiente', 'indigena', 'raizal',
          'palenquero', 'gitano', 'sin reconocimiento']
estratos = [1, 2, 3, 4, 5, 6]
continuan = 0
sinreconocimiento = 0
afrodescendiente = 0
indigena = 0
raizal = 0
palenquero = 0
gitano = 0

for personas in range(cantidad):
    etnia = input('ingresa etnia: ')
    estrato = int(input('ingreso estrato: '))
    ingreso = int(input('ingrese el ingreso: '))

    if etnia not in etnias or estrato not in estratos:
        continue

    # declaración de variables
    puntaje_etnia = 0
    puntaje_estrato = 0
    puntaje_ingreso = 0
    total = 0
    smlv = 908526

    # Verificacion de la etnia
    if etnia == 'afrodescendiente':
        puntaje_etnia = 8
        afrodescendiente += 1
    elif etnia == 'indigena':
        puntaje_etnia = 10
        indigena += 1
    elif etnia == 'raizal':
        puntaje_etnia = 12
        raizal += 1
    elif etnia == 'palenquero':
        puntaje_etnia = 14
        palenquero += 1
    elif etnia == 'gitano':
        puntaje_etnia = 16
        gitano += 1
    elif etnia == 'sinreconocimiento':
        puntaje_etnia = 0
        sinreconocimiento += 1

    # Verificar el estrato
    if estrato == 1:
        puntaje_estrato = 20
    elif estrato == 2:
        puntaje_estrato = 16
    elif etnia == 3:
        puntaje_estrato = 12
    elif estrato == 4:
        puntaje_estrato = 8
    elif estrato == 5 or estrato == 6:
        puntaje_estrato = 0

    # Verificar ingreso
    if ingreso < smlv:
        puntaje_ingreso = 30
    elif ingreso < (2 * smlv):
        puntaje_ingreso = 18
    elif ingreso < (smlv * 4):
        puntaje_ingreso = 14
    elif ingreso < (smlv * 5):
        puntaje_ingreso = 8
    elif ingreso >= (smlv * 5):
        puntaje_ingreso = 0

    # print(puntaje_etnia, puntaje_estrato, puntaje_ingreso)
    # hago la sumatoria de puntajes
    total = puntaje_etnia + puntaje_estrato + puntaje_ingreso
    # print(total)

    if total >= 50:
        continuan += 1  # continuan = continuan + 1

print(continuan)
print("sin reconocimiento", sinreconocimiento)
print("afrodescendiente", afrodescendiente)
print("indigena", indigena)
print("raizal", raizal)
print("palenquero", palenquero)
print("gitano", gitano)
