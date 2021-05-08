'''
ejercicio2:
haga un algoritmo que dado un numero de maximo 4 digitos(si se ingresa
un numeo de menos digitos o de mas debe avisar que no se puede)
permita sumar la descomposicion de sus digitos:
ej:numero: 4123
4 + 1 + 2 + 3 =10
ej : numero: 445  (NO SE PUEDE)
ej : numero: 78967 (no se puede)
'''
numero = int(input('Ingrese un numero: '))

#En este rango se considera que el numero es de menos de 4 cifras
if numero < 1000 and numero >= -999:
    print("El numero debe ser de 4 cifras")

# Numero de 4 cifras positivos
elif numero >= 1000 and numero <= 9999:
    num4 = numero % 10
    num3 = numero % 100 // 10
    num2 = numero % 1000 // 100
    num1 = numero % 10000 // 1000
    suma = num1 + num2 + num3 + num4
    print("La suma de los digitos es:", suma)

# Numero de 4 cifras negativo
elif numero <= -1000 and numero >= -9999:
    numero = abs(numero)
    num4 = numero % 10
    num3 = numero % 100 // 10
    num2 = numero % 1000 // 100
    num1 = numero % 10000 // 1000
    suma = num1 + num2 + num3 + num4
    print("La suma de los digitos es: -", suma)
else:
    print("El numero debe ser de 4 cifras")