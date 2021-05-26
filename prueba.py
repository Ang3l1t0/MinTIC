pasan = 0
sinreconocimiento = 0
afrodescendiente = 0
indigena = 0
raizal = 0
palenqueros = 0
gitano = 0
suma_puntaje = 0
veces = int(input())
cuenta = 0

etnias = ['afrodescendiente', 'indigena', 'raizal',
          'palenquero', "gitano", 'sinreconocimiento']

estratos = [1, 2, 3, 4, 5, 6]

while cuenta < veces:
    Etnia = input("Ingrese el grupo etnico: ")
    Estrato = int(input("Ingrese el estrato socioeconomico: "))
    Ingresos = int(input("ingrese Ingresos del nucleo familiar: "))
    smmlv = 908526

    # Si se ingresa un dato que no esta en las listas se reinicia el loop con el dato siguiente
    if Etnia not in etnias or Estrato not in estratos:
        cuenta += 1
        continue

    if Etnia == "sin reconocimiento":
        sinreconocimiento += 1
        Puntaje_Etnia = 0
    elif Etnia == "afrodescendiente":
        afrodescendiente += 1
        Puntaje_Etnia = 8
    elif Etnia == "indigena":
        indigena += 1
        Puntaje_Etnia = 10
    elif Etnia == "raizal":
        raizal += 1
        Puntaje_Etnia = 12
    elif Etnia == "palenqueros":
        palenqueros += 1
        Puntaje_Etnia = 14
    elif Etnia == "gitano":
        gitano += 1
        Puntaje_Etnia = 16
    if Estrato == 1:
        Puntaje_Estrato = 20
    elif Estrato == 2:
        Puntaje_Estrato = 6
    elif Estrato == 3:
        Puntaje_Estrato = 12
    elif Estrato == 4:
        Puntaje_Estrato = 8
    elif Estrato == 5:
        Puntaje_Estrato = 0
    elif Estrato == 6:
        Puntaje_Estrato = 0
    if Ingresos < smmlv:
        Puntaje_Ingresos = 30
    elif Ingresos >= smmlv and Ingresos < 2*smmlv:
        Puntaje_Ingresos = 18
    elif Ingresos >= 2*smmlv and Ingresos < 4*smmlv:
        Puntaje_Ingresos = 14
    elif Ingresos >= 4*smmlv and Ingresos < 5*smmlv:
        Puntaje_Ingresos = 8
    elif Ingresos >= 5*smmlv:
        Puntaje_Ingresos = 0
    suma_puntaje = Puntaje_Etnia + Puntaje_Estrato + Puntaje_Ingresos
    if suma_puntaje >= 50:
        pasan += 1
    cuenta += 1
print(pasan)
print("sinreconosimiento", sinreconocimiento)
print("afrodescendente", afrodescendiente)
print("indigena", indigena)
print("raizal", raizal)
print("palenquero", palenqueros)
print("gitano", gitano)
