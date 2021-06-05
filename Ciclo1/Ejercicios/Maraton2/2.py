'''
Crear una aplicación de me llene una lista con n números aleatorios
(se deben generar automáticamente) posterior a esto se debe ingresar un número 
de búsqueda en esa lista para ver si ese número existe. Tendrá solo 3 intentos para encontrar
el numero si lo encuentra en esos 3 intentos debe decir que lo encontró y en qué posición lo encontró. 
De lo contrario le dirá que perdió.
'''
import random
numero_elementos = int(input('Ingrese el numero de elementos en la lista: '))
lst = []


def find_element(n):
    print('Haz encontrado el numero {} en el indice {}.'.format(n, lst.index(n)))


for i in range(numero_elementos):
    numero = random.randint(1, 100)
    lst.append(numero)

print(lst)

for intento in range(3):
    dato = int(input('Ingrese un numero: '))
    if dato in lst:
        find_element(dato)
        break
    else:
        print('sigue intentando')
