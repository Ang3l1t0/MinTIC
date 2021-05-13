valor_compra = float(input('Ingrese el valor de la compra: $'))
if valor_compra >= 0 and valor_compra <= 1000000:
    descuento = 1
elif valor_compra > 1000000:
    descuento = 0.8

if valor_compra < 0:
    print('ERROR: datos invalidos')
else:
    total = valor_compra * descuento
    print('valor a pagar es: $', total)
