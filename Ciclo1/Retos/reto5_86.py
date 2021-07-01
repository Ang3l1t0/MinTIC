
import csv
from operator import itemgetter

def sorter(item):
    # Since highest marks first, least error = most marks
    ingresopro = item[1]
    etnia = item[0]
    return (ingresopro, etnia)

contador=0
suma_ing = 0
afro=0
git=0
sinr=0
indi=0
raiz=0
pale=0
lista=[]
lista1=[] 
archivo=open('./data.csv')
lector = csv.reader(archivo, delimiter=",")
# Reto 5 sin encabezado
next(lector, None)
ciudad=input()
for fila in lector:
    ingreso=int(fila[6])
    # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
    if fila[2]==ciudad and fila[7]=="1":
        lista1.append(int(fila[6]))
        contador+=1
        suma_ing += ingreso
        float = suma_ing / contador
        promedio_ing = "{:.2f}".format(float)
        if fila[4]=="afrodescendiente":
            afro=afro+1
        if fila[4]=="indigena":
            indi=indi+1
        if fila[4]=="raizal":
            raiz=raiz+1 
        if fila[4]=="palenquero":
            pale=pale+1
        if fila[4]=="gitano":
            git=git+1
        if fila[4]=="sin reconocimiento":
            sinr=sinr+1
lista.append(["sin reconocimiento",int(sinr)])
lista.append(["afrodescendiente",int(afro)])
lista.append(["indigena",int(indi)])
lista.append(["raizal",int(raiz)])
lista.append(["palenquero",int(pale)])
lista.append(["gitano",int(git)])
orden=sorted(lista, key=itemgetter(1), reverse=True)

#orden=sorted(lista, key=sorter, reverse=True)

Vmin=(min(lista1))
Vmax=(max(lista1))
print(contador)
print (Vmin,Vmax,promedio_ing)
for s in orden:
    if s[1]!=0:
        print(s)
archivo.close()