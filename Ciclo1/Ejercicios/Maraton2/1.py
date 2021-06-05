'''
Crear una aplicación que me llene una lista de números de N elementos y a partir de ella genera otra 
lista con cada uno de los números factoriales de cada uno de los elementos de la primera lista.
Ej:
Original=[2,3,5]
Factoriales=[1x2 , 1x2x3 , 1x2x3x4x5]
'''
import math

# Solicito numero de elementos que tendra la lista original y declaración de listas vacias
numero_elementos = int(input('Ingrese el numero de elementos: '))
lst = []
factoriales = []

#funcion que calcula el factorial de un numero
def calculo_factorial(n):
    return(math.factorial(n))

# creo la lista lst de acuerdo al numero de elementos que se solicitaron
for i in range(numero_elementos):
    numero = int(input('Ingrese un numero: '))
    lst.append(numero)

# calculo el factorial de cada elemento de la lista lst y lo añado a la lista factorial
for i in lst:
    factoriales.append(calculo_factorial(i))

# Imprimo resultados
print(lst)
print(factoriales)
