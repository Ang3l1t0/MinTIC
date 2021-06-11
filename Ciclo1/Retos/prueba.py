import numpy as np
import collections
participantes = int(input())

etnias = []
estratos = []
ingresos = []
lEtnias = ["sin reconocimiento", "afrodescendiente",
           "indigena", "raizal", "palenquero", "gitano"]


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


def menosXdia(matriz):
    ''' Imprime las etnias que menos se presentaron por día'''
    for i in range(7):
        # elemento ordenado e indice de ese elemento
        u, indices = np.unique(matriz[:, i], return_inverse=True)
        # valor minimo de una lista ordenado con el numero de repeticiones de cada numero
        conteo = u[np.argmin(np.bincount(indices))]
        # usamos el numero obtenido para obtener el nombre de la etnia en la lista
        matriz_min = lEtnias[int(conteo) - 1]
        if i < 6:
            print(matriz_min, end=",")
        if i == 6:
            print(matriz_min, end="\n")


etnias = lista_matriz(participantes)
menosXdia(etnias)