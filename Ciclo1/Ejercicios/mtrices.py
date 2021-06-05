'''
EJERCICIO DE PRACTICA MATRICES.

Haga un programa que me capture una
matriz de 'N' filas y 'M' columnas y a 
partir de ella me genere un vector que
contengan los numeros primos de esa matriz.
validar el caso de que no encuentre ningun
primo en la matriz.
'''
filas = int(input('Ingrese numero de filas: '))
columnas = int(input('Ingrese numero de columnas: '))
mat = []

for i in range(0, filas):
    for j in range(0, columnas):
        numero = int(input('Ingrese un numero: '))
        mat.append(numero)
        
print(mat)