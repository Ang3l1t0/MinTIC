import numpy as np
participantes = int(input())

etnias = []
estratos = []
ingresos = []
lEtnias = ["sin reconocimiento", "afrodescendiente",
           "indigena", "raizal", "palenquero", "gitano"]
lEstratos = ["1", "2", "3", "4", "5", "6"]


def lista_matriz(filas):
    ''' Funcion para crear una matriz de etnias tipo numpy'''
    matriz = []
    for _i in range(filas):
        lst = input().split()
        matriz.append(lst)
    for _i in range(7):
        for _x in range(filas):
            matriz = np.array(matriz)
    return matriz


def Xdia(matriz, masOmenos):
    ''' Imprime las etnias que menos se presentaron por día'''
    for i in range(7):
        # elemento ordenado e indice de ese elemento
        u, indices = np.unique(matriz[:, i], return_inverse=True)
        # valor minimo o maximo de una lista ordenado con el numero de repeticiones de cada numero
        if masOmenos == 'menos':
            conteo = u[np.argmin(np.bincount(indices))]
        elif masOmenos == 'mas':
            conteo = u[np.argmax(np.bincount(indices))]
        # usamos el numero obtenido para obtener el nombre de la etnia en la lista
        etniaXdia = lEtnias[int(conteo) - 1]
        if i < 6:
            print(etniaXdia, end=",")
        if i == 6:
            print(etniaXdia, end="\n")


def Xsemana(matriz, masOmenos):
    ''' Imprime las etnias que menos se presentaron por semana'''
    # elemento ordenado e indice de ese elemento
    u, indices = np.unique(matriz, return_inverse=True)
    # valor minimo o max de una lista ordenado con el numero de repeticiones de cada numero
    if masOmenos == "menos":
        conteo = u[np.argmin(np.bincount(indices))]
    elif masOmenos == "mas":
        conteo = u[np.argmax(np.bincount(indices))]
    # usamos el numero obtenido para obtener el nombre de la etnia en la lista
    semana_min = lEtnias[int(conteo) - 1]
    print(semana_min)


def cont_noCon(matriz1, matriz2, matriz3):
    lContinuan = []
    puntaje = 0
    pEtnia = 0
    pEstrato = 0
    pSalario = 0
    smlv = 908526
    for columnas in range(7):
        continua = 0
        for filas in range(participantes):
            etnia = (matriz1[filas][columnas])
            estrato = (matriz2[filas][columnas])
            salario = int(matriz3[filas][columnas])
            # Verificacion de la etnia
            if etnia not in lEstratos or estrato not in lEstratos or salario < 0:
                break
            else:
                if etnia == '2':
                    pEtnia = 8
                elif etnia == '3':
                    pEtnia = 10
                elif etnia == '4':
                    pEtnia = 12
                elif etnia == '5':
                    pEtnia = 14
                elif etnia == '6':
                    pEtnia = 16
                elif etnia == '1':
                    pEtnia = 0

                # Verificacion del estrato
                if estrato == "1":
                    pEstrato = 20
                elif estrato == "2":
                    pEstrato = 16
                elif estrato == "3":
                    pEstrato = 12
                elif estrato == "4":
                    pEstrato = 8
                elif estrato == "5" or estrato == "6":
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
        lContinuan.append(continua)
    print(lContinuan[0], lContinuan[1], lContinuan[2],
          lContinuan[3], lContinuan[4], lContinuan[5], lContinuan[6])


# LLamado de metodos y PROCEDIMIENTOS
etnias = lista_matriz(participantes)
estratos = lista_matriz(participantes)
ingresos = lista_matriz(participantes)
Xdia(etnias, "menos")
Xsemana(etnias, "menos")
Xdia(etnias, "mas")
Xsemana(etnias, "mas")
cont_noCon(etnias, estratos, ingresos)
