'''
contara letra por letra y la guarde cuantas veces se repite en la palabra
'''
palabra = input('Introduzca la palabra: ')

for l in palabra:
    print('La letra ' + str(l) + ' se repite ' +
          str(palabra.count(l)) + ' veces')
