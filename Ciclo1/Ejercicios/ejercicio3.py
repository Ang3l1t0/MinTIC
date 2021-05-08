'''
haga un algoritmo que dado un numero me informe si este numero es:

1)par y positivo
2)par y negativo
3)impar y positivo
4)impar y negativo
'''

numero = int(input('Ingrese un numero: '))

if numero >= 0 and numero % 2 == 0:
    print('El numero es par y positivo')
elif numero > 0 and numero % 2 != 0:
    print('El numero es impar y positivo')
elif numero < 0 and numero % 2 != 0:
    print('El numero es impar y negativo')
elif numero < 0 and numero % 2 == 0:
    print('El numero es par y negativo')
