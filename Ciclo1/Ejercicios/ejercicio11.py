'''
ejercicio2:
haga un programa que capture un texto cualquiera y haga lo 
siguiente:
1)contar la cantidad de vocales mayusculas y/o minusculas
  que encontro
2)contar las consonantes mayusculas y/o minusculas que 
encontro
3) contar los simbolos especiales que encontro
4)informar cual fue la mayor busqueda
'''
texto = input('Ingrese texto: ').lower()
vocales = 0
consonantes = 0
especial = 0
maximo = 0
for i in texto:
    if i in ('a', 'e', 'i', 'o', 'u'):
        vocales += 1
    elif i in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        consonantes += 1
    else:
        especial += 1
#    if texto.count(i):
#        maximo += 1 
print('la cantidad de vocales es', vocales)
print('la cantidad de consonantes es', consonantes)
print('la cantidad de caracteres especiales es', especial)
#print('el caracter que mas se repite es', )