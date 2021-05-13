kilos = float(input('Ingrese cuantos kilos va a comprar: '))
precio_kilo = float(input('Ingrese el valor del kilo: '))

if kilos >= 0 and kilos < 2:
    descuento = 1
elif kilos >= 2 and kilos < 5:
    descuento = 0.9
elif kilos >= 5 and kilos < 10:
    descuento = 0.85
elif kilos >= 10:
    descuento = 0.8

print(kilos * (descuento * precio_kilo))
