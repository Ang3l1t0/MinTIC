'''
Crear un vector que almacene los nombres de N personas y a partir de ese genere 
otro vector de 5 posiciones con (cantidad de vocales, cantidad de consonantes, 
cantidad de números, cantidad de espacios en blanco, cantidad de símbolos especiales) 
ENTRE todos los nombres registrados.
'''
cantidad = int(input('Ingrese el numero de personas: '))
nombres = []
datos = []
vocales = 0
def contar_vocales(palabra):
    voc = 0
    for c in palabra:
        if c in "aeiouAEIOU":
            voc = voc + 1
    return voc

for _i in range(cantidad):
    nombre = input('Ingrese el nombre: ')
    nombres.append(nombre)

for j in nombres:
    print(vocales)
    vocales = contar_vocales(j)
    vocales += vocales
    
print(contar_vocales("ana"))
print(nombres)
print(vocales)
