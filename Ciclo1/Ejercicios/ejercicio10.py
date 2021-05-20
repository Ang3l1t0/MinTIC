'''
ejercicio1:
haga un programa que permita generar las tablas de multiplicar
del rango de tablas que el usuario indique.
ej:
tabla inicial:5
tabla final:7

5x1=5
5x2=10
5x3=15
.
.
.
5x10=50
-----------
6x1=6
6x2=12
.
.
-----------
7x1=7
7x2=
.
.
'''

t1 = int(input('Tabla inicial: '))
t2 = int(input('Tabla final: '))

for i in range(t1, t2 + 1):
    for j in range(1, 11):
        total = i * j
        #print('{} x {} = {}'.format(i, j, total))
        print(i, ' X ', j, ' = ', total)
