antiguedad = float(input('Ingrese el numero de años de antiguedad: '))
utilidad = float(input('Ingrese la utilidad: '))

if antiguedad < 1:
    porc = 0.05
elif antiguedad >= 1 and antiguedad < 2:
    porc = 0.07
elif antiguedad >= 2 and antiguedad < 5:
    porc = 0.1
elif antiguedad >= 5 and antiguedad <= 10:
    porc = 0.15
elif antiguedad > 10:
    porc = 0.25
print(utilidad * porc)
