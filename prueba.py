import numpy as np

participantes = int(input())
etnias = []
lEtnias = ["sin reconocimiento", "afrodescendiente",
           "indigena", "raizal", "palenquero", "gitano"]


def lista_matriz(filas):
    ''' Funcion para crear una matriz de etnias tipo numpy'''
    matriz = []
    # Recibe el numero dado de personas y los añade a una lista de listas matriz
    for _i in range(filas):
        lst = input().split()
        matriz.append(lst)
    # convierte la lista de listas en una matriz numpy y retorna esa matriz
    for _i in range(7):
        for _x in range(filas):
            matriz = np.array(matriz)
    return matriz


def Xdia(matriz):
    ''' Imprime las etnias que menos se presentaron por día'''
    for i in range(7):
        # elemento ordenado e indice de ese elemento
        u, indices = np.unique(matriz[:, i], return_inverse=True)
        # valor minimo o maximo de una lista ordenado con el numero de repeticiones de cada numero
        # if masOmenos == 'menos':
        conteo = u[np.argmin(np.bincount(indices))]
        # elif masOmenos == 'mas':
        #    conteo = u[np.argmax(np.bincount(indices))]
        # usamos el numero obtenido para obtener el nombre de la etnia en la lista
        etniaXdia = lEtnias[int(conteo) - 1]
        if i < 6:
            print(etniaXdia, end=",")
        if i == 6:
            print(etniaXdia, end="\n")


def Xsemana(matriz):
    ''' Imprime las etnias que menos se presentaron por semana'''
    # elemento ordenado e indice de ese elemento
    u, indices = np.unique(matriz, return_inverse=True)
    print(u)
    print(indices)
    # valor minimo o max de una lista ordenado con el numero de repeticiones de cada numero
    #if masOmenos == "menos":
    conteo = u[np.argmin(np.bincount(indices))]
    print(conteo)
    #elif masOmenos == "mas":
    #    conteo = u[np.argmax(np.bincount(indices))]
    # usamos el numero obtenido para obtener el nombre de la etnia en la lista
    semana_min = lEtnias[int(conteo) - 1]
    print(semana_min)


etnias = lista_matriz(participantes)
#Xdia(etnias)
Xsemana(etnias)