'''
1) Se debe realizar un muestreo con N personas para determinar el promedio de peso de los ninos, 
jóvenes, adultos y viejos que existen en su zona habitacional.
Se determinan las categorías así:
CATEGORIA	EDAD
ninos		0 - 12
Jóvenes	13 - 29
Adultos		30 - 59
Viejos		60 en adelante
'''
ninos = 0
jovenes = 0
adultos = 0
viejos = 0
prom_ninos = 0
prom_jovenes = 0
prom_adultos = 0
prom_viejos = 0
while True:
    dato = input('Desea ingresar un dato [s][n]: ')

    if dato == "s" or dato == "S":
        edad = int(input('Ingrese la edad: '))
        peso = float(input('Ingrese el peso en kilos: '))

        if edad >= 0 and edad <= 12:
            ninos += 1
            prom_ninos += peso
        elif edad >= 13 and edad <= 29:
            jovenes += 1
            prom_jovenes += peso
        elif edad >= 30 and edad <= 59:
            adultos += 1
            prom_adultos += peso
        elif edad >= 60:
            viejos += 1
            prom_viejos += peso
    elif dato == 'n' or dato == 'N':
        print(prom_ninos)
        if ninos == 0:
            print('Promedio de peso de niños es: 0')
        else:
            print('Promedio de peso de niños es:', (prom_ninos / ninos))
        if jovenes == 0:
            print('Promedio de peso de jovenes es: 0')
        else:
            print('Promedio de peso de jovenes es:', (prom_jovenes / jovenes))
        if adultos == 0:
            print('Promedio de peso de adultos es: 0')
        else:
            print('Promedio de peso de adultos es:', (prom_adultos / adultos))
        if viejos == 0:
            print('Promedio de peso de viejos es: 0')
        else:
            print('Promedio de peso de viejos es:', (prom_viejos / viejos))
        break
    else:
        print('Introduzca un opcion valida')
