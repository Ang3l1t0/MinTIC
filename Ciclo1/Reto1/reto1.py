while True:
    etnia = input("Pertenece a algun grupo etnico? ")
    etnias = ['afrodescendiente', 'indigena', 'raizal',
              'palenquero', 'gitano', 'sinreconocimiento']

    estratos = [1, 2, 3, 4, 5, 6]

    if etnia not in etnias:
        print("Se presento un error")
        break
    estrato = int(input("Indique su estrato: "))
    if estrato not in estratos:
        print("Se presento un error")
        break

    salario = int(input("Ingrese su salario: "))
    puntaje = 0
    pEtnia = 0
    pEstrato = 0
    pSalario = 0
    # Verificacion de la etnia
    if etnia == 'afrodescendiente':
        pEtnia = 8
    if etnia == 'indigena':
        pEtnia = 10
    if etnia == 'raizal':
        pEtnia = 12
    if etnia == 'palenquero':
        pEtnia = 14
    if etnia == 'gitano':
        pEtnia = 16
    if etnia == 'sinreconocimiento':
        pEtnia = 0

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
    else:
        print("Se presento un error")

    # Verificacion del salario
    if salario / 908526 < 1:
        pSalario = 30
    elif salario / 908526 < 2:
        pSalario = 18
    elif salario / 908526 < 4:
        pSalario = 14
    elif salario / 908526 < 5:
        pSalario = 8
    elif salario / 908526 >= 5:
        pSalario = 0

    puntaje = pEtnia + pEstrato + pSalario
    # print(pEtnia, pEstrato, pSalario)
    # print(puntaje)
    if puntaje >= 50:
        print("El candidato continua en el proceso de seleccion")
    else:
        print("El candidato no continua en el proceso de seleccion")
