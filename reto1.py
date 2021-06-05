etnia = input('ingresa etnia: ')
estrato = int(input('ingreso estrato: '))
ingreso = int(input('ingrese el ingreso: '))

# declaración de variables
puntaje_etnia = 0
puntaje_estrato = 0
puntaje_ingreso = 0
total = 0
smlv = 908526
etnias = ['afrodescendiente', 'indigena', 'raizal',
          'palenquero', 'gitano', 'sinreconocimiento']
estratos = [1, 2, 3, 4, 5, 6]

if etnia not in etnias or estrato not in estratos:
    print('Se presento un error')

# Verificacion de la etnia
if etnia == 'afrodescendiente':
    puntaje_etnia = 8
elif etnia == 'indigena':
    puntaje_etnia = 10
elif etnia == 'raizal':
    puntaje_etnia = 12
elif etnia == 'palenquero':
    puntaje_etnia = 14
elif etnia == 'gitano':
    puntaje_etnia = 16
elif etnia == 'sinreconocimiento':
    puntaje_etnia = 0

# Verificar el estrato
if estrato == 1:
    puntaje_estrato = 20
elif estrato == 2:
    puntaje_estrato = 16
elif etnia == 3:
    puntaje_estrato = 12
elif estrato == 4:
    puntaje_estrato = 8
elif estrato == 5 or estrato == 6:
    puntaje_estrato = 0


# Verificar ingreso
if ingreso < smlv:
    puntaje_ingreso = 30
elif ingreso < (2 * smlv):
    puntaje_ingreso = 18
elif ingreso < (smlv * 4):
    puntaje_ingreso = 14
elif ingreso < (smlv * 5):
    puntaje_ingreso = 8
elif ingreso >= (smlv * 5):
    puntaje_ingreso = 0

# print(puntaje_etnia, puntaje_estrato, puntaje_ingreso)
# hago la sumatoria de puntajes
total = puntaje_etnia + puntaje_estrato + puntaje_ingreso
# print(total)

if total >= 50:
    print("El candidato continua en el proceso de seleccion")
else:
    print("El candidato no continua en el proceso de seleccion")
