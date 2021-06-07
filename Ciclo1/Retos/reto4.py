from numpy.lib.arraysetops import unique
from operator import itemgetter

# semanas recibe un numero que sera usado para obtener el numero de filas de la matriz
semanas = int(input())

# Declaraciones
etnias = []
estratos = []
ingresos = []


def lista_etnias(filas):
    ''' Funcion para crear una matriz de etnias'''
    for _i in range(filas):
        lst = input().split()
        etnias.append(lst)
    return etnias


def lista_estratos(filas):
    ''' Funcion para crear una matriz de estratos'''
    for _i in range(filas):
        lst = input().split()
        estratos.append(lst)
    return estratos


def lista_ingresos(filas):
    ''' Funcion para crear una matriz de ingresos'''
    for _i in range(filas):
        lst = input().split()
        ingresos.append(lst)
    return ingresos


def menosXdia(matriz):
    '''retorna la etnia que menos se presentó por dia'''
    day1 = []
    day2 = []
    day3 = []
    day4 = []
    day5 = []
    day6 = []
    day7 = []
    for i in range(7):
        for fila in matriz:
            if i == 0:
                day1.append(fila[i])
            elif i == 1:
                day2.append(fila[i])
            elif i == 2:
                day3.append(fila[i])
            elif i == 3:
                day4.append(fila[i])
            elif i == 4:
                day5.append(fila[i])
            elif i == 5:
                day6.append(fila[i])
            elif i == 6:
                day7.append(fila[i])
    
    etnia1 = count_element(day1)
    etnia2 = count_element(day2)
    etnia3 = count_element(day3)
    etnia4 = count_element(day4)
    etnia5 = count_element(day5)
    etnia6 = count_element(day6)
    etnia7 = count_element(day7)
    print(f'{etnia1},{etnia2},{etnia3},{etnia4},{etnia5},{etnia6},{etnia7}')
    #return(day1, day2, day3, day4, day5, day6, day7)


def count_element(lista):
    '''Imprime el elemento que menos se repite en una lista'''
    cuenta = 0
    lista1 = []
    for i in lista:
        cuenta = lista.count(i)
        if i == '1':
            #sinreconocimiento += 1
            sr = ('sin reconocimiento', 1, cuenta)
            lista1.append(sr)
        elif i == '2':
            ad = ('afrodescendiente', 2, cuenta)
            lista1.append(ad)
        elif i == '3':
            ig = ('indigena', 3, cuenta)
            lista1.append(ig)
        elif i == '4':
            rz = ('raizal', 4, cuenta)
            lista1.append(rz)
        elif i == '5':
            pq = ('palenquero', 5, cuenta)
            lista1.append(pq)
        elif i == '6':
            gt = ('gitano', 6, cuenta)
            lista1.append(gt)
    etnia = sorted(lista1, key=itemgetter(2, 1))
    return etnia[0][0]


# almaceno el resultado de las funciones anteriores en sus respectivas variables
etnia = lista_etnias(semanas)
estrato = lista_estratos(semanas)
ingreso = lista_ingresos(semanas)

menosXdia(etnia)
# print(etnia)
# print(estrato)
# print(ingreso)
#print(days)
