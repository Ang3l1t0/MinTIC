'''
Crear una aplicación de capture 2 vectores diferentes del mismo tamaño y genere 
automáticamente un tercer vector con los elementos intercalados del primer con el segundo vector.
Ej:
A=[10,20,30,40]
B=[50,60,70,80]
C=[10,50,20,60,30,70,40,80]
'''
import random
tamaño = int(input('Ingrese el tamaño del vector: '))
lst1 = []
lst2 = []
lst3 = []

for i in range(tamaño):
    v1 = random.randint(1, 100)
    v2 = random.randint(1, 100)
    lst1.append(v1)
    lst2.append(v2)

print(lst1)
print(lst2)

for i in range(tamaño):
    lst3.append(lst1[i])
    lst3.append(lst2[i])

print(lst3)
